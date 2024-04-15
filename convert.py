import base64
import zlib

blueprint_string = input('Insert blueprint string:')
blueprint_string = blueprint_string[1:]
blueprint_string = base64.b64decode(blueprint_string)
blueprint_string = zlib.decompress(blueprint_string)
blueprint_string = blueprint_string.decode('utf-8')

converted_blueprint = (blueprint_string.replace('straight-rail', 'straight-space-rail')
                       .replace('curved-rail', 'curved-space-rail'))
converted_blueprint = converted_blueprint.encode('utf-8')
converted_blueprint = zlib.compress(converted_blueprint, 9)
converted_blueprint = '0' + base64.b64encode(converted_blueprint).decode('utf-8')

print('Converted blueprint:\n' + converted_blueprint)
