from pycaw.pycaw import AudioUtilities


class VolumeController:

    def __init__(self):
        # Get the default Windows audio device
        devices = AudioUtilities.GetSpeakers()
        self.volume = devices.EndpointVolume

    def set_volume(self, percentage):
        """
        Set Windows volume from 0 to 100 percent.
        """

        # Make sure percentage stays between 0 and 100
        percentage = max(0, min(100, percentage))

        # PyCaw uses a value between 0.0 and 1.0
        volume_level = percentage / 100

        # Set the Windows volume
        self.volume.SetMasterVolumeLevelScalar(
            volume_level,
            None
        )

    def get_volume(self):
        """
        Get current Windows volume as a percentage.
        """

        current_volume = self.volume.GetMasterVolumeLevelScalar()

        return int(current_volume * 100)