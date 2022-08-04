import tensorflow as tf
import skimage as ski


def fen_from_onehot(one_hot):
    piece_symbols = 'prbnkqPRBNKQ'
    output = ''
    for j in range(8):
        for i in range(8):
            if(one_hot[j][i] == 12):
                output += ' '
            else:
                output += piece_symbols[one_hot[j][i]]
        if(j != 7):
            output += '-'

    for i in range(8, 0, -1):
        output = output.replace(' ' * i, str(i))

    return output


def get_tiles_from_image(image):
    square_size = 50
    img_read = ski.io.imread(image)
    tiles = ski.util.view_as_blocks(
        img_read, block_shape=(square_size, square_size, 3))
    tiles = tiles.squeeze(axis=2)
    return tiles.reshape(64, square_size, square_size, 3)


def process_image(image):
    tiles = get_tiles_from_image(image)
    return tiles


def predict(image):
    model = tf.keras.models.load_model('./baseline.h5')
    pred = model.predict(get_tiles_from_image(
        image)).argmax(axis=1).reshape(-1, 8, 8)
    fen = fen_from_onehot(pred[0])
    return fen
