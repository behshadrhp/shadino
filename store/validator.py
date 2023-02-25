from django.core.exceptions import ValidationError


def validate_image_file(file):
    max_size_kb = 200

    if file.size > max_size_kb * 1024:
        raise ValidationError(f'حجم این فایل بیشتر از حد مجاز است')


