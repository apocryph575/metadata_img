import exif


def image_metadata(image_path):
    # check image metadata
    with open(image_path, "rb") as palm_1_file:
        exif_data = exif.Image(palm_1_file)
        all_attributes = exif_data.get_all()
    if exif_data.has_exif:
        status = f"contains EXIF (version {exif_data.exif_version}) information."
    else:
        status = "does not contain any EXIF information."
    print(f"Image {status}")

    # Show all attributes
    for tag, value in all_attributes.items():
        print(f"{tag}: {value}")


def main():
    image_path = 'images/test.jpg'
    image_metadata(image_path)


if __name__ == '__main__':
    main()
