import base64
import zlib
import pyperclip

blueprint_string = input('Paste your blueprint string:\n')
blueprint_string = blueprint_string[1:]
blueprint_string = base64.b64decode(blueprint_string)
blueprint_string = zlib.decompress(blueprint_string)
blueprint_string = blueprint_string.decode('utf-8')

converted_blueprint = (blueprint_string.replace('straight-rail', 'se-space-straight-rail')
                       .replace('curved-rail', 'se-space-curved-rail')
                       .replace('landfill', 'se-space-platform-scaffold')
                       .replace('express-transport-belt', 'se-space-transport-belt')
                       .replace('express-underground-belt', 'se-space-underground-belt')
                       .replace('express-splitter', 'se-space-splitter')
                       .replace('pipe', 'se-space-pipe')
                       .replace('pipe-to-ground', 'se-space-pipe-to-ground')
                       .replace('assembling-machine-3', 'se-space-assembling-machine'))
converted_blueprint = converted_blueprint.encode('utf-8')
converted_blueprint = zlib.compress(converted_blueprint, 9)
converted_blueprint = '0' + base64.b64encode(converted_blueprint).decode('utf-8')

pyperclip.copy(converted_blueprint)
print('Your converted blueprint has been copied to clipboard!')
