# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os

class Flexi(Package):
    """FLEXI: A high order unstructured solver for hyperbolic-parabolic
    coservation laws based on the discontinuous Galerkin spectral 
    element method."""
  
    homepage = "https://www.flexi-project.org"
    git      = "https://github.com/flexi-framework/flexi"
  
    version('master',  branch='master')
  
    variant('mpi', default=True,
            description='Builds a parallel version of FLEXI')
  
    depends_on('hdf5 fortran=True mpi=True',  when='+mpi', type='build')
    depends_on('hdf5 fortran=True mpi=False', when='~mpi', type='build')
    depends_on('mpi', when='+mpi', type='build')
    depends_on('cmake', type='build')
    depends_on('lapack', type='build')
  
    def cmake_args(self):
        args = []
      
        if '+mpi' in self.spec:
            args.append('-DFLEXI_MPI=ON')
        else:
            args.append('-DFLEXI_MPI=OFF')
      
        args.append('-DFLEXI_BUILD_HDF5=OFF')
        args.append('-DFLEXI_BUILD_POSTI=OFF')
        return args
  
    def install(self, spec, prefix):
        mkdir(prefix.bin)
        mkdir(prefix.lib)
        with working_dir('spack-build', create=True):
            cmake('..', *self.cmake_args())
            make('flexi')
            # the flexi install step does nothing, so here manually install all the binaries and libs
            for binary in os.listdir('bin'):
                install(join_path('bin',binary),join_path(prefix.bin,binary))
            for lib in os.listdir('lib'):
                install(join_path('lib',lib),join_path(prefix.lib,lib))
