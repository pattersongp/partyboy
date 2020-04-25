from django.db import models

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'party_{0}/{1}'.format(instance.party_id, filename)

class Picture(models.Model):
    party_id = models.ForeignKey(
        'party.Party',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to=user_directory_path)
