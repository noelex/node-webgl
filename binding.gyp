{
	'variables': {
	},
	'targets': [{
		'target_name': 'webgl',
		'sources': [
			'src/cpp/attrib.cpp',
			'src/cpp/bindings.cpp',
			'src/cpp/blend.cpp',
			'src/cpp/buffers.cpp',
			'src/cpp/framebuffers.cpp',
			'src/cpp/instances.cpp',
			'src/cpp/programs.cpp',
			'src/cpp/renderbuffers.cpp',
			'src/cpp/shaders.cpp',
			'src/cpp/stencil.cpp',
			'src/cpp/textures.cpp',
			'src/cpp/transformfeedback.cpp',
			'src/cpp/uniform.cpp',
			'src/cpp/vertexarrays.cpp',
			'src/cpp/webgl.cpp',
		],
		'defines': ['UNICODE', '_UNICODE'],
		'cflags_cc': ['-std=c++17', '-fno-exceptions'],
		'cflags': ['-fno-exceptions'],
		'include_dirs': [
			"<!(node -p \"require('node-addon-api').include_dir\")",
		],
		'conditions': [
			['OS=="linux"', {
				'cflags': [
					'<!@(pkg-config --cflags epoxy)',
				],
				'ldflags': [
					'<!@(pkg-config --libs-only-L --libs-only-other epoxy)',
				],
				'libraries': [
					'<!@(pkg-config --libs-only-l epoxy)',
				],
				'defines': ['__linux__'],
			}],
			['OS=="mac"', {
				'libraries': [
					'-Wl,-rpath,@loader_path',
					'-Wl,-rpath,@loader_path/../node_modules/deps-opengl-raub/<(bin)',
					'-Wl,-rpath,@loader_path/../../deps-opengl-raub/<(bin)',
					'<(gl_bin)/glew.dylib',
				],
				'MACOSX_DEPLOYMENT_TARGET': '10.9',
				'defines': ['__APPLE__'],
				'CLANG_CXX_LIBRARY': 'libc++',
				'OTHER_CFLAGS': ['-std=c++17', '-fno-exceptions'],
			}],
			['OS=="win"', {
				'libraries': ['glew32.lib', 'opengl32.lib'],
				'defines': ['WIN32_LEAN_AND_MEAN', 'VC_EXTRALEAN', '_WIN32', '_HAS_EXCEPTIONS=0'],
				'msvs_settings' : {
					'VCCLCompilerTool' : {
						'AdditionalOptions' : [
							'/O2','/Oy','/GL','/GF','/Gm-', '/std:c++17',
							'/EHa-s-c-','/MT','/GS','/Gy','/GR-','/Gd',
						],
					},
					'VCLinkerTool' : {
						'AdditionalOptions' : ['/DEBUG:NONE', '/LTCG', '/OPT:NOREF'],
					},
				},
			}],
		],
	}]
}
