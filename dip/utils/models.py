def user_to_json(user):
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'second_name': user.second_name,
        'patronymic': user.patronymic,
        'phone_number': user.phone_number,
        'photo': user.photo,
        'role': user.role,
        'job_title': user.job_title,
    }