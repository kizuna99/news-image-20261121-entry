"""Publish the committed poster in the contest sandbox.

The poster is committed beside this file; the sandbox only needs it copied
to the output directory under the fixed name entry.png, byte for byte.
"""
import os
from pathlib import Path
from struct import unpack_from


def main():
    image = Path(__file__).with_name('entry.png').read_bytes()
    if not 33 <= len(image) <= 1_048_576 or not image.startswith(b'\x89PNG\r\n\x1a\n'):
        raise ValueError('Expected a PNG poster of at most 1 MiB')
    if image[12:16] != b'IHDR' or unpack_from('>II', image, 16) != (1024, 1024):
        raise ValueError('Expected a 1024 x 1024 poster')
    if not image.endswith(b'IEND\xaeB`\x82'):
        raise ValueError('Expected a complete PNG ending with an IEND chunk')
    output = Path(os.environ.get('MAKEFUN_OUTPUT_DIR') or '/output')
    output.mkdir(parents=True, exist_ok=True)
    (output / 'entry.png').write_bytes(image)


if __name__ == '__main__':
    main()
