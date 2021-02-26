project(
  'ChatApp',
  'cpp',
  version: '0.0.1',
  license: 'AGPL',
  meson_version: '>=0.56.0',
  default_options: ['cpp_std=c++17']
)

defs = [
  '-DNONEXISTENT_UWEBSOCKETS=1',
  '-DEXISTENT_WEBSOCKETPP=1',
  '-DEXISTENT_OPUS=1',
  '-DEXISTENT_ASIO=1',
  '-DEXISTENT_CPR=1'
]

# Set up sleepy-discord subproject
cmake = import('cmake')

opt_var = cmake.subproject_options()
opt_var.add_cmake_defines({'ONLY_SLEEPY_DISCORD': true, 'ENABLE_VOICE': false})
opt_var.append_compile_args('cpp', defs, '-fPIC')

sd = cmake.subproject('sleepy-discord', options: opt_var)
sd_lib = sd.dependency('sleepy-discord')

executable(
  'bot',
  'src/main.cpp',
  dependencies: [
    dependency('openssl'),
    dependency('cpr'),
    dependency('websocketpp'),
    dependency('asio'),
    dependency('opus'),
    sd_lib
  ],
  cpp_args: defs
)
