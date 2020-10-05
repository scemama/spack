# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import inspect

from spack.directives import depends_on, extends
from spack.package import PackageBase, run_after
from spack.util.executable import Executable


class OpamPackage(PackageBase):
    """Specialized class for packages that are built using OPAM, the OCaml
    package manager.

    For more information on OPAM, see:
    https://opam.ocaml.org

    This class provides a single phase that can be overridden:

        1. :py:meth:`~.OpamPackage.install`

    It has sensible defaults, and for many packages the only thing
    necessary will be to add dependencies
    """
    phases = ['install']

    #: This attribute is used in UI queries that need to know the build
    #: system base class
    build_system_class = 'OpamPackage'

    extends('opam')

    depends_on('opam', type=('build', 'run'))


