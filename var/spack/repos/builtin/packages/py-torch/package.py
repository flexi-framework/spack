# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


# TODO: try switching to CMakePackage for more control over build
class PyTorch(PythonPackage):
    """Tensors and Dynamic neural networks in Python
    with strong GPU acceleration."""

    homepage = "https://pytorch.org/"
    git      = "https://github.com/pytorch/pytorch.git"
    install_time_test_callbacks = ['install_test', 'import_module_test']

    maintainers = ['adamjstewart']
    import_modules = [
        'tools', 'caffe2', 'torch', 'tools.cwrap', 'tools.autograd',
        'tools.setup_helpers', 'tools.shared', 'tools.jit', 'tools.pyi',
        'tools.nnwrap', 'tools.cwrap.plugins', 'caffe2.core', 'caffe2.proto',
        'caffe2.python', 'caffe2.distributed', 'caffe2.perfkernels',
        'caffe2.experiments', 'caffe2.contrib', 'caffe2.quantization',
        'caffe2.core.nomnigraph', 'caffe2.python.ideep', 'caffe2.python.mint',
        'caffe2.python.layers', 'caffe2.python.onnx', 'caffe2.python.trt',
        'caffe2.python.models', 'caffe2.python.docs', 'caffe2.python.modeling',
        'caffe2.python.mkl', 'caffe2.python.examples',
        'caffe2.python.predictor', 'caffe2.python.helpers',
        'caffe2.python.rnn', 'caffe2.python.onnx.bin',
        'caffe2.python.models.seq2seq', 'caffe2.experiments.python',
        'caffe2.contrib.nnpack', 'caffe2.contrib.warpctc',
        'caffe2.contrib.nccl', 'caffe2.contrib.playground',
        'caffe2.contrib.gloo', 'caffe2.contrib.script', 'caffe2.contrib.prof',
        'caffe2.contrib.tensorboard', 'caffe2.contrib.aten',
        'caffe2.contrib.playground.resnetdemo',
        'caffe2.contrib.script.examples', 'caffe2.contrib.aten.docs',
        'caffe2.quantization.server', 'torch.nn', 'torch.onnx',
        'torch.distributed', 'torch.autograd', 'torch.multiprocessing',
        'torch.cuda', 'torch.backends', 'torch.optim', 'torch.utils',
        'torch.contrib', 'torch.jit', 'torch.sparse',
        'torch.for_onnx', 'torch._thnn', 'torch.distributions',
        'torch.nn.parallel', 'torch.nn._functions', 'torch.nn.backends',
        'torch.nn.utils', 'torch.nn.modules', 'torch.nn.parallel.deprecated',
        'torch.nn._functions.thnn', 'torch.distributed.deprecated',
        'torch.autograd._functions', 'torch.backends.cuda',
        'torch.backends.mkl', 'torch.backends.mkldnn', 'torch.backends.openmp',
        'torch.backends.cudnn', 'torch.utils.backcompat',
        'torch.utils.bottleneck', 'torch.utils.ffi', 'torch.utils.tensorboard',
        'torch.utils.data', 'torch.utils.data._utils'
    ]

    version('master', branch='master', submodules=True)
    version('1.3.1', tag='v1.3.1', submodules=True)
    version('1.3.0', tag='v1.3.0', submodules=True)
    version('1.2.0', tag='v1.2.0', submodules=True)
    version('1.1.0', tag='v1.1.0', submodules=True)
    version('1.0.1', tag='v1.0.1', submodules=True)
    version('1.0.0', tag='v1.0.0', submodules=True)
    version('0.4.1', tag='v0.4.1', submodules=True)
    version('0.4.0', tag='v0.4.0', submodules=True)
    version('0.3.1', tag='v0.3.1', submodules=True)

    variant('cuda', default=True, description='Enables CUDA build')
    variant('cudnn', default=True, description='Enables the cuDNN build')
    variant('magma', default=False, description='Enables the MAGMA build')
    variant('fbgemm', default=False, description='Enables the FBGEMM build')
    variant('test', default=False, description='Enables the test build')
    variant('miopen', default=False, description='Enables the MIOpen build')
    variant('mkldnn', default=True, description='Enables use of MKLDNN')
    variant('nnpack', default=False, description='Enables NNPACK build')
    variant('qnnpack', default=False, description='Enables QNNPACK build (quantized 8-bit operators)')
    variant('distributed', default=False, description='Enables distributed (c10d, gloo, mpi, etc.) build')
    variant('nccl', default=True, description='Use Spack-installed NCCL')
    variant('caffe2', default=False, description='Enables Caffe2 operators build')
    variant('gloo', default=False, description='Enables features related to distributed support')
    variant('opencv', default=False, description='Enables use of OpenCV for additional operators')
    variant('openmp', default=True, description='Enables use of OpenMP for parallelization')
    variant('ffmpeg', default=False, description='Enables use of ffmpeg for additional operators')
    variant('leveldb', default=False, description='Enables use of LevelDB for storage')
    variant('lmdb', default=False, description='Enables use of LMDB for storage')
    variant('binary', default=False, description='Enables the additional binaries/ build')
    variant('redis', default=False, description='Use Redis for distributed workflows')
    variant('zstd', default=False, description='Enables use of ZSTD')
    variant('tbb', default=False, description='Enables TBB support')

    conflicts('+cudnn', when='~cuda')
    conflicts('+magma', when='~cuda')
    conflicts('+fbgemm', when='@:0.4')
    conflicts('+miopen', when='@:0.4')
    conflicts('+mkldnn', when='@:0.3')
    conflicts('+qnnpack', when='@:0.4')
    conflicts('+nccl', when='~cuda')
    conflicts('+opencv', when='@:0.4')
    conflicts('+ffmpeg', when='@:0.4')
    conflicts('+leveldb', when='@:0.4')
    conflicts('+lmdb', when='@:0.4')
    conflicts('+binary', when='@:0.4')
    conflicts('+redis', when='@:1.0')
    conflicts('+zstd', when='@:1.0')
    conflicts('+tbb', when='@:1.1')

    # Required dependencies
    depends_on('cmake@3.5:', type='build')
    # Use Ninja generator to speed up build times
    # Automatically used if found
    depends_on('ninja@1.5:', type='build')
    depends_on('python@2.7:2.8,3.5:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-future', when='@1.1: ^python@:2', type='build')
    depends_on('py-pyyaml', type=('build', 'run'))
    depends_on('py-typing', when='@0.4: ^python@:3.4', type=('build', 'run'))
    depends_on('py-pybind11', when='@0.4:', type=('build', 'run'))
    depends_on('blas')
    depends_on('lapack')
    depends_on('protobuf', when='@0.4:')
    depends_on('eigen', when='@0.4:')
    # TODO: replace all third_party packages with Spack packages

    # Optional dependencies
    depends_on('cuda@7.5:', when='+cuda', type=('build', 'link', 'run'))
    depends_on('cuda@9:', when='@1.1:+cuda', type=('build', 'link', 'run'))
    depends_on('cudnn@6:', when='+cudnn')
    depends_on('cudnn@7:', when='@1.1:+cudnn')
    depends_on('magma', when='+magma')
    # TODO: add dependency: https://github.com/pytorch/FBGEMM
    depends_on('fbgemm', when='+fbgemm')
    # TODO: add dependency: https://github.com/ROCmSoftwarePlatform/MIOpen
    depends_on('miopen', when='+miopen')
    depends_on('mkl', when='+mkldnn')
    # TODO: add dependency: https://github.com/Maratyszcza/NNPACK
    depends_on('nnpack', when='+nnpack')
    depends_on('qnnpack', when='+qnnpack')
    depends_on('mpi', when='+distributed')
    depends_on('nccl', when='+nccl')
    depends_on('gloo', when='+gloo')
    depends_on('opencv', when='+opencv')
    depends_on('llvm-openmp', when='%clang platform=darwin +openmp')
    depends_on('ffmpeg', when='+ffmpeg')
    depends_on('leveldb', when='+leveldb')
    depends_on('lmdb', when='+lmdb')
    depends_on('redis', when='+redis')
    depends_on('zstd', when='+zstd')
    depends_on('tbb', when='+tbb')

    # Test dependencies
    depends_on('py-hypothesis', type='test')
    depends_on('py-six', type='test')
    depends_on('py-psutil', type='test')

    # Both build and install run cmake/make/make install
    # Only run once to speed up build times
    phases = ['install']

    def setup_build_environment(self, env):
        def enable_or_disable(variant, keyword='USE', var=None, newer=False):
            """Set environment variable to enable or disable support for a
            particular variant.

            Parameters:
                variant (str): the variant to check
                keyword (str): the prefix to use for enabling/disabling
                var (str): CMake variable to set. Defaults to variant.upper()
                newer (bool): newer variants that never used NO_*
            """
            if var is None:
                var = variant.upper()

            # Version 1.1.0 switched from NO_* to USE_* or BUILD_*
            # But some newer variants have always used USE_* or BUILD_*
            if self.spec.satisfies('@1.1:') or newer:
                if '+' + variant in self.spec:
                    env.set(keyword + '_' + var, 'ON')
                else:
                    env.set(keyword + '_' + var, 'OFF')
            else:
                if '+' + variant in self.spec:
                    env.unset('NO_' + var)
                else:
                    env.set('NO_' + var, 'ON')

        # Build system has problems locating MKL libraries
        # See https://github.com/pytorch/pytorch/issues/24334
        if 'mkl' in self.spec:
            env.prepend_path('CMAKE_PREFIX_PATH', self.spec['mkl'].prefix.mkl)

        # Build in parallel to speed up build times
        env.set('MAX_JOBS', make_jobs)

        # Spack logs have trouble handling colored output
        env.set('COLORIZE_OUTPUT', 'OFF')

        # Don't use vendored third-party libraries
        env.set('BUILD_CUSTOM_PROTOBUF', 'OFF')
        env.set('USE_PYTORCH_QNNPACK', 'OFF')
        env.set('USE_SYSTEM_EIGEN_INSTALL', 'ON')
        env.set('pybind11_DIR', self.spec['py-pybind11'].prefix)
        env.set('pybind11_INCLUDE_DIR',
                self.spec['py-pybind11'].prefix.include)

        enable_or_disable('cuda')
        if '+cuda' in self.spec:
            env.set('CUDA_HOME', self.spec['cuda'].prefix)

        enable_or_disable('cudnn')
        if '+cudnn' in self.spec:
            env.set('CUDNN_LIB_DIR', self.spec['cudnn'].libs.directories[0])
            env.set('CUDNN_INCLUDE_DIR', self.spec['cudnn'].prefix.include)
            env.set('CUDNN_LIBRARY', self.spec['cudnn'].libs[0])

        enable_or_disable('fbgemm')
        enable_or_disable('test', keyword='BUILD')

        if '+miopen' in self.spec:
            env.set('MIOPEN_LIB_DIR', self.spec['miopen'].libs.directories[0])
            env.set('MIOPEN_INCLUDE_DIR', self.spec['miopen'].prefix.include)
            env.set('MIOPEN_LIBRARY', self.spec['miopen'].libs[0])

        enable_or_disable('mkldnn')
        if '+mkldnn' in self.spec:
            env.set('MKLDNN_HOME', self.spec['intel-mkl'].prefix)

        enable_or_disable('nnpack')
        enable_or_disable('qnnpack')
        enable_or_disable('distributed')

        enable_or_disable('nccl')
        enable_or_disable('nccl', var='SYSTEM_NCCL')
        if '+nccl' in self.spec:
            env.set('NCCL_ROOT', self.spec['nccl'].prefix)
            env.set('NCCL_LIB_DIR', self.spec['nccl'].libs.directories[0])
            env.set('NCCL_INCLUDE_DIR', self.spec['nccl'].prefix.include)

        enable_or_disable('caffe2', keyword='BUILD', var='CAFFE2_OPS')
        enable_or_disable('gloo', newer=True)
        enable_or_disable('opencv', newer=True)
        enable_or_disable('openmp', newer=True)
        enable_or_disable('ffmpeg', newer=True)
        enable_or_disable('leveldb', newer=True)
        enable_or_disable('lmdb', newer=True)
        enable_or_disable('binary', keyword='BUILD', newer=True)

        env.set('PYTORCH_BUILD_VERSION', self.version)
        env.set('PYTORCH_BUILD_NUMBER', 0)

        # BLAS to be used by Caffe2
        if '^mkl' in self.spec:
            env.set('BLAS', 'MKL')
        elif '^atlas' in self.spec:
            env.set('BLAS', 'ATLAS')
        elif '^openblas' in self.spec:
            env.set('BLAS', 'OpenBLAS')
        elif '^veclibfort' in self.spec:
            env.set('BLAS', 'vecLib')
        elif '^libflame' in self.spec:
            env.set('BLAS', 'FLAME')
        elif '^eigen' in self.spec:
            env.set('BLAS', 'Eigen')

        enable_or_disable('redis', newer=True)
        enable_or_disable('zstd', newer=True)
        enable_or_disable('tbb', newer=True)

    def test(self):
        pass

    def install_test(self):
        with working_dir('test'):
            python('run_test.py')
