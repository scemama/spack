# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class NcclTests(MakefilePackage, CudaPackage):
    """These tests check both the performance and
       the correctness of NCCL operations."""

    homepage = "https://github.com/NVIDIA/nccl-tests"
    url      = "https://github.com/NVIDIA/nccl-tests/archive/v2.0.0.tar.gz"

    version('2.0.0', sha256='731fc3b7c37de59cfe880bf198349ac185639ef23570749ea6aef334c850c49c')

    variant('mpi', default=True, description='with MPI support')
    variant('cuda', default=True, description='with CUDA support, must be true')
    conflicts('~cuda', msg='nccl-tests require cuda')

    depends_on('nccl')
    depends_on('cuda')
    depends_on('mpi', when='+mpi')

    @property
    def build_targets(self):
        targets = []
        targets.append('CUDA_HOME={0}'.format(self.spec['cuda'].prefix))
        targets.append('NCCL_HOME={0}'.format(self.spec['nccl'].prefix))
        if '+mpi' in self.spec:
            targets.append('MPI_HOME={0}'.format(self.spec['mpi'].prefix))
            targets.append('MPI=1')
        return targets

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install_tree('./build', prefix.bin)
