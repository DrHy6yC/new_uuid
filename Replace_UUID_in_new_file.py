import re
import uuid

from itertools import groupby

with open('new_test.txt', 'w', encoding="utf-8") as nf:
    with open('test.txt', 'r', encoding="utf-8") as f:
        body_forms = f.read()
    uuid_extract_pattern = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    id_forms = re.findall(uuid_extract_pattern, body_forms)
    id_forms = [el for el, _ in groupby(id_forms)]
    print(id_forms)

    for i in id_forms:
        new_id = str(uuid.uuid4()) 
        body_forms = body_forms.replace(i, new_id)

    print(body_forms)
    nf.write(body_forms)
 
