INPUTSTREAM_PROTOCOLS = {
    'mpd': 'inputstream.adaptive',
    'ism': 'inputstream.adaptive',
    'hls': 'inputstream.adaptive',
    'rtmp': 'inputstream.rtmp'
}

DRM_SCHEMES = {
    'widevine': 'widevine',
    'com.widevine.alpha': 'widevine'
}

CDM_EXTENSIONS = (
    '.so',
    '.dll',
    '.dylib'
)

X86_MAP = {
    'x86_64': 'x86_64',
    'AMD64': 'x86_64',
    'x86': 'x86',
    'i386': 'x86',
    'i686': 'x86'
}

WIDEVINE_SUPPORTED_ARCHS = [
    'x86_64',
    'x86',
    'armv7',
    'armv8',
    'aarch64',
    'aarch64_be'
]

WIDEVINE_ARCH_MAP_X86 = {
    'x86_64': 'x64',
    'x86': 'ia32'
}

WIDEVINE_OS_MAP = {
    'Linux': 'linux',
    'Windows': 'win',
    'Darwin': 'mac'
}

WIDEVINE_SUPPORTED_OS = [
    'Android',
    'Linux',
    'Windows',
    'Darwin'
]

WIDEVINE_MINIMUM_KODI_VERSION = {
    'Android': '18.0',
    'Windows': '17.4',
    'Linux': '17.4',
    'Darwin': '17.4'
}

WIDEVINE_CURRENT_VERSION_URL = 'https://dl.google.com/widevine-cdm/current.txt'

WIDEVINE_DOWNLOAD_URL = 'https://dl.google.com/widevine-cdm/{0}-{1}-{2}.zip'

WIDEVINE_LICENSE_FILE = 'LICENSE.txt'

WIDEVINE_MANIFEST_FILE = 'manifest.json'

WIDEVINE_CONFIG_NAME = 'widevine_config.json'

CHROMEOS_RECOVERY_CONF = 'https://dl.google.com/dl/edgedl/chromeos/recovery/recovery.conf'

CHROMEOS_ARM_HWID = 'SPRING'

CHROMEOS_BLOCK_SIZE = 512

HLS_MINIMUM_IA_VERSION = '2.0.10'
