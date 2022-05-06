STATIC_DATA = {
    'test': {
        'normal_user': {
            'username': 'test_user_641143',
            'password': 'Password'
        }
    }
}


def get_static_data(env='test', key=None):
    try:
        return STATIC_DATA[env][key]
    except Exception:
        raise NotImplementedError
