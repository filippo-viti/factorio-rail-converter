import base64
import zlib

blueprint_string = input('Insert blueprint string:')
blueprint_string = blueprint_string[1:]
blueprint_string = base64.b64decode(blueprint_string)

blueprint_string = zlib.decompress(blueprint_string)
blueprint_string = blueprint_string.decode('utf-8')

print('Converted blueprint:\n' + blueprint_string)
