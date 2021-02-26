project(
  'ChatApp',
  'cpp',
  version: '0.0.1',
  license: 'AGPL',
  meson_version: '>=0.56.0',
  default_options: ['cpp_std=c++17']
)

cmake = import('cmake')

comp = meson.get_compiler('cpp')

### Sleepy-Discord ###

sd_defs = [
  'NONEXISTENT_UWEBSOCKETS=1',
  'EXISTENT_WEBSOCKETPP=1',
  'EXISTENT_OPUS=1',
  'EXISTENT_ASIO=1',
  'EXISTENT_CPR=1'
]

if comp.get_argument_syntax() == 'msvc'
  ignore_warns = '/w'
  def_flag = '/D'
else
  ignore_warns = '-w'
  def_flag = '-D'
endif

sd_flags = []
foreach def : sd_defs
  sd_flags += def_flag + def
endforeach

sd_cmake_opts = cmake.subproject_options()
sd_cmake_opts.add_cmake_defines({'ONLY_SLEEPY_DISCORD': true})
sd_cmake_opts.append_compile_args('cpp', sd_flags, ignore_warns, pic: true)

sd = cmake.subproject('sleepy-discord', options: sd_cmake_opts)
sd_lib = declare_dependency(
  compile_args: sd_flags,
  dependencies: sd.dependency('sleepy-discord', include_type: 'system')
)

### Bot ###

executable('bot',
  'src/main.cpp',
  dependencies: [
    dependency('fmt'),
    dependency('openssl'),
    dependency('cpr'),
    dependency('websocketpp'),
    dependency('asio'),
    dependency('opus'),
    sd_lib
  ]
)
