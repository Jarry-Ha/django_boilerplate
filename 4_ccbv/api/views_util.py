def obj_to_post(obj):
    # obj 객체 -> dict 로 변환
    post = dict(vars(obj))

    # convert to string
    if obj.modify_dt:
        post['modify_dt'] = obj.modify_dt.strftime('%Y-%m-%d %H:%M')
    else:
        post['modify_dt'] = ''

    if obj.owner:
        post['owner'] = obj.owner.username
    else:
        post['owner'] = 'Anonymous'

    del post['_state']

    return post