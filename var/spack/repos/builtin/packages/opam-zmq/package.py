from spack import *

class OpamZmq(OpamPackage):
    """This library contains basic bindings for zmq.
Lwt aware bindings to zmq are availble though package zmq-lwt
Async aware bindings to zmq are availble though package zmq-async

Api documentation can be found at https://issuu.github.io/ocaml-zmq
"""

    homepage = "https://github.com/issuu/ocaml-zmq"
    url      = "https://raw.githubusercontent.com/ocaml/opam-repository/master/packages/zmq/zmq.5.1.3/opam"
#    url      = "https://github.com/issuu/ocaml-zmq/releases/download/5.1.3/zmq-5.1.3.tar.gz"

    maintainers = ['scemama']

    version('5.1.3', sha256='f51303aa9443d745a5154fe40817fda4ee8ed99c0375003ad359eade26112580', expand=False)

#    version('5.1.3', sha256='40877896e96accf4aaad10c6e303763087cad4cb1308afcaed012cb5a815e708')
#    version('5.1.2', sha256='9bea821945e5b39b2b44a1741aef06edccf8e8fcb0eec09c07e397e410cf7712')
#    version('5.1.1', sha256='c16703b80533eb2a74d26c3eab9b57a1c3172ebc9a9e3877264c1d7b009b6c2a')
#    version('5.1.0', sha256='ce181f098112352b9dc5f8126b8d5ec25b867bc69b6098c0f5ce5cfad2e0e43e')
#    version('5.0.0', sha256='831f7f9c206dc9fdbdf037c70907eeaa2716ac2502cf33fd6212f3e91d1fa924')
#    version('4.0-8', sha256='7c31a0522fb940fabc0a5dee38774ec2d9cf588b2a4302af0e8f531b5d964682')
#    version('4.0-7', sha256='8d62b0582ff44342966587bdede4090687cc24959117bb93e1bbffad659e67f7')
#    version('4.0-6', sha256='1dd2c722e3d7d7c5c48c9c44585749470374d45b54ead8a76e2e47cdb19b7b45')
#    version('4.0-5', sha256='fc83e346fe8d2e36ffb7c7d00e961cccf6bb1c5d77d03339e0ec684da8cba784')
#    version('4.0-4', sha256='1b86e512d5835b37a9b9dccf6015851dbd6df19dee84cb83db9e0eb61271e787')

    depends_on('opam', type=('build','run'))
    depends_on('ocaml', type=('build', 'run'))
    depends_on('libzmq', type=('build', 'run'))
    depends_on('pkgconfig', type=('build','run'))


    def setup_environment(self, spack_env, run_env):
        spack_env.set('C_INCLUDE_PATH', self.spec['libzmq'].headers.directories[0])
        spack_env.set('LIBRARY_PATH', self.spec['libzmq'].libs.directories[0])

    def install(self, spec, prefix):
        opam = Executable("opam")
        opam('install', '--yes', 'zmq')

