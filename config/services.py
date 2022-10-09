def get_path_upload_avatar(instance, file):
    '''Постоение пути к файлуб format: (media)/avatar/user_id/pthoto.jpg'''
    return f'avatar/{instance.id}/{file}'