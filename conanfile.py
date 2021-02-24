from conans import ConanFile, tools, Meson
import os

class ConanFileToolsTest(ConanFile):
    name = 'ChatApp'
    version = '0.0.1'
    generators = 'pkg_config'
    requires = ['openssl/1.1.1j', 'cpr/1.5.2', 'websocketpp/0.8.2']
    settings = 'os', 'compiler', 'build_type'

    def build(self):
        meson = Meson(self)
        meson.configure(build_folder='build')
        meson.build()
