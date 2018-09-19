import subprocess
import sys

import versioneer


def is_version_tag():
    root = versioneer.get_root()
    cfg = versioneer.get_config_from_root(root)
    pieces = versioneer.git_pieces_from_vcs(
        tag_prefix=cfg.tag_prefix,
        root=root,
        verbose=False,
    )

    return pieces['distance'] == 0


def main():
    print('Version: {}'.format(versioneer.get_version()))
    if not is_version_tag():
        print(
            'Versioneer did not report zero distance to a version tag,'
            ' aborting.',
        )
        return

    command = [
        sys.executable,
        '-m', 'twine',
    ]
    command.extend(sys.argv[1:])

    return subprocess.call(command)


if __name__ == '__main__':
    sys.exit(main())
