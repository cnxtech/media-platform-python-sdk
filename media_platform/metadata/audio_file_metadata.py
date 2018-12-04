from media_platform.metadata.audio.audio_basic import AudioBasic
from media_platform.metadata.file_metadata import FileMetadata, MediaType
from media_platform.service.file_descriptor import FileDescriptor


class AudioFileMetadata(FileMetadata):
    def __init__(self, file_descriptor, basic=None):
        # type: (FileDescriptor, AudioBasic) -> None
        super(AudioFileMetadata, self).__init__(MediaType.audio, file_descriptor, basic)

    @classmethod
    def deserialize(cls, data):
        # type: (dict) -> AudioFileMetadata
        if data['mediaType'] != MediaType.audio:
            raise ValueError('not audio metadata')

        file_descriptor = FileDescriptor.deserialize(data['fileDescriptor'])
        basic = AudioBasic.deserialize(data.get('basic')) if data.get('basic') else None

        return AudioFileMetadata(file_descriptor, basic)
