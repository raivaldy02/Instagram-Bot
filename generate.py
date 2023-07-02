import uuid

cookies = {
    'ig_did': 'A42CEA2B-28BC-4834-8944-D03CC591CC60',
    'ig_nrcb': '1',
    'mid': 'ZBa4aAAEAAGLxvjM1hq4c7-lpe3l',
    'datr': 'ZrgWZOsUxFyjHR28BBbzmRws',
    'dpr': '1',
    'ds_user_id': '37559473228',
    'shbid': '"7044\\05437559473228\\0541717493752:01f712edd7a30f017c7ac77d84c2827289b5d5f0d9a86ef0368c4be1350bd5f57c0ec871"',
    'shbts': '"1685957752\\05437559473228\\0541717493752:01f78b8fa1830643b99d31b26d55028d72850c8e4f9da64da08bef6896db475a6b9c9716"',
    'csrftoken': '8mAScBrNAgFVlcHbuV8ZTUWjLVqeS1aP',
    'sessionid': '37559473228%3AFduYRMpBxx0Sqn%3A10%3AAYfEaNZtzb2PG6b0dCzPmfn4gbclTNXrPqLZ83VnDQ',
    'rur': '"CCO\\05437559473228\\0541717535052:01f7f23321bdbc9c47bddaaf148b679d4ae3aebcc9752c8d99dc612ba264a6d7b5269495"',
}

def generate_uuid(return_hex=False, seed=None):
    """
    Generate uuid

    :param return_hex: Return in hex format
    :param seed: Seed value to generate a consistent uuid
    :return:
    """
    if seed:
        m = hashlib.md5()
        m.update(seed.encode("utf-8"))
        new_uuid = uuid.UUID(m.hexdigest())
    else:
        new_uuid = uuid.uuid1()
    if return_hex:
        return new_uuid.hex
    return str(new_uuid)

@staticmethod
def authenticated_params():
    return {
        "_csrftoken": cookies.get("csrftoken"),
        "_uuid": generate_uuid(return_hex = False),
        "_uid": cookies.get("ds_user_id")
    }