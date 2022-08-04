import streamlit as st

from predict import predict


def main():
    st.set_page_config(layout="wide")
    st.subheader("Upload the image of the chess board")
    board_image = st.file_uploader('Upload image', type='jpeg')

    uploaded_image = st.empty()
    result = st.empty()

    predict_button = st.button(
        label="Identify positions", key="classify_button")

    if predict_button and board_image is None:
        result.error("Please upload an image")
    elif predict_button and board_image is not None:
        result.text("Identifying positions...")
        prediction = predict(board_image)
        uploaded_image.image(board_image, width=200)
        result.write(prediction)


if __name__ == '__main__':
    main()
