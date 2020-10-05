# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install opam-ocaml
#
# You can edit this file again by typing:
#
#     spack edit opam-ocaml
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *

class OpamOcaml(OpamPackage):
    """OCaml is an industrial strength programming language supporting
       functional, imperative and object-oriented styles.

       The compiler is installed via the OPAM packet manager."""

    homepage = "http://ocaml.org/"
    url      = "https://caml.inria.fr/pub/distrib/ocaml-4.06/ocaml-4.06.0.tar.gz"

    maintainers = ['scemama']

    version('4.11.0', sha256='b5bd04bf794a676389b167633f01f8275acdd853149b137f7575f2c2ddef1377')
    version('4.10.0', sha256='58d431dde66f5750ebe9b15d5a1c4872f80d283dec23448689b0d1a498b7e4c7')
    version('4.09.0', sha256='2b728f8a0e90da14f22fdc04660f2ab33819cdbb12bff0ceae3fdbb0133cf7a6')
    version('4.08.1', sha256='ee50118ee88472fd4b64311fa560f8f8ab66a1899f0117815c69a16070980f78')
    version('4.08.0', sha256='e6e244f893f2070ebcdeac0637fbe2054fd82deebefefa3e3ed85a405cd4ecd8')
    version('4.07.1', sha256='2ad43be17ed5c74ea27887ae0cc4793b835408180c0b9175bc9ad53082a59af4')
    version('4.07.0', sha256='50e10b0c4e28300cb889e56839ec9e07e2847a85e04bfbd5a7ed0290b7239ef8')
    version('4.06.1', sha256='0c38c6f531103e87fab1c218a7e76287d7cb4d7ee4dea64e7f85952af3b1b50e')
    version('4.06.0', sha256='c17578e243c4b889fe53a104d8927eb8749c7be2e6b622db8b3c7b386723bf50')
    version('4.03.0', sha256='7fdf280cc6c0a2de4fc9891d0bf4633ea417046ece619f011fd44540fcfc8da2')

    patch('fix-duplicate-defs.patch', when="@4.08.0:4.09.0 %gcc@10.0:")
    depends_on('ncurses')
    depends_on('opam')

    def install(self, spec, prefix):
        base_args = ['-prefix', '{0}'.format(prefix)]

        # This patch is aarch64-linux-fj only.
        # However, similar patch is needed for other arch/OS/compiler
        # to use correct assembler. (See #17918)
        if self.spec.satisfies('%fj'):
            filter_file(
                'aspp="${toolpref}clang -c -Wno-trigraphs"',
                'aspp="{0} -c"'.format(spack_cc),
                'configure',
                string=True
            )
            if self.spec.satisfies('@4.11.0:'):
                filter_file(
                    'as="${toolpref}clang -c -Wno-trigraphs"',
                    'as="${toolpref}as"',
                    'configure',
                    string=True
                )

        opam = Executable("opam")
        opam('install', '.')
