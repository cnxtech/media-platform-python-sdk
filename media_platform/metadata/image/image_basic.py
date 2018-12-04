from media_platform.lang.serialization import Deserializable


class ImageBasic(Deserializable):
    def __init__(self, width, height, image_format, color_space=None):
        # type: (int, int, str, str) -> None
        super(ImageBasic, self).__init__()
        self.width = int(width) if width else None
        self.height = int(height) if height else None
        self.format = image_format
        self.color_space = color_space

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> ImageBasic
        return ImageBasic(data['width'], data['height'], data['format'], data.get('colorspace'))
