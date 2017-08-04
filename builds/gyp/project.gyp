################################################################################
#  THIS FILE IS 100% GENERATED BY ZPROJECT; DO NOT EDIT EXCEPT EXPERIMENTALLY  #
#  Read the zproject/README.md for information about making permanent changes. #
################################################################################
#   GYP file for CZMQ
#   gyp --depth=.
{
  'target_defaults': {
    'include_dirs': [
      '../../../libzmq/include',
      '../../include',
      '.'
    ],
    'defines': [
      'CZMQ_GYP_BUILD'
    ],
    'conditions': [
      [ 'OS=="win"', {
        'defines': [
          'CZMQ_HAVE_WINDOWS',
          'ZMQ_STATIC',
          'CZMQ_STATIC'
        ],
        'libraries': [
          'ws2_32',
          'advapi32',
          'iphlpapi',
          'Rpcrt4'
        ]
      }],
      [ 'OS=="mac"', {
        'defines': [
          'CZMQ_HAVE_OSX'
        ]
      }],
      [ 'OS=="linux"', {
        'defines': [
          'CZMQ_HAVE_LINUX'
        ],
        'xcode_settings': {
          'OTHER_CFLAGS': [
            '-fPIC'
          ],
        },
        'libraries': [
          '-lpthread'
        ]
      }]
    ]
  },
  'targets': [
    {
      'target_name': 'libczmq',
      'type': 'static_library',
      'sources': [
        'platform.h',
        '../../include/czmq.h',
        '../../include/czmq_prelude.h',
        '../../src/zactor.c',
        '../../include/zactor.h',
        '../../src/zargs.c',
        '../../include/zargs.h',
        '../../src/zarmour.c',
        '../../include/zarmour.h',
        '../../src/zauth.c',
        '../../include/zauth.h',
        '../../src/zbeacon.c',
        '../../include/zbeacon.h',
        '../../src/zcert.c',
        '../../include/zcert.h',
        '../../src/zcertstore.c',
        '../../include/zcertstore.h',
        '../../src/zchunk.c',
        '../../include/zchunk.h',
        '../../src/zclock.c',
        '../../include/zclock.h',
        '../../src/zconfig.c',
        '../../include/zconfig.h',
        '../../src/zdigest.c',
        '../../include/zdigest.h',
        '../../src/zdir.c',
        '../../include/zdir.h',
        '../../src/zdir_patch.c',
        '../../include/zdir_patch.h',
        '../../src/zfile.c',
        '../../include/zfile.h',
        '../../src/zframe.c',
        '../../include/zframe.h',
        '../../src/zgossip.c',
        '../../include/zgossip.h',
        '../../src/zgossip_msg.c',
        '../../src/zgossip_msg.h',
        '../../src/zhash.c',
        '../../include/zhash.h',
        '../../src/zhashx.c',
        '../../include/zhashx.h',
        '../../src/ziflist.c',
        '../../include/ziflist.h',
        '../../src/zlist.c',
        '../../include/zlist.h',
        '../../src/zlistx.c',
        '../../include/zlistx.h',
        '../../src/zloop.c',
        '../../include/zloop.h',
        '../../src/zmonitor.c',
        '../../include/zmonitor.h',
        '../../src/zmsg.c',
        '../../include/zmsg.h',
        '../../src/zpoller.c',
        '../../include/zpoller.h',
        '../../src/zproc.c',
        '../../include/zproc.h',
        '../../src/zproxy.c',
        '../../include/zproxy.h',
        '../../src/zrex.c',
        '../../include/zrex.h',
        '../../src/zsock.c',
        '../../include/zsock.h',
        '../../src/zstr.c',
        '../../include/zstr.h',
        '../../src/zsys.c',
        '../../include/zsys.h',
        '../../src/ztimerset.c',
        '../../include/ztimerset.h',
        '../../src/ztrie.c',
        '../../include/ztrie.h',
        '../../src/zuuid.c',
        '../../include/zuuid.h',
        '../../src/foreign/sha1/sha1.h',
        '../../src/foreign/sha1/sha1.inc_c',
        '../../src/foreign/slre/readme.txt',
        '../../src/foreign/slre/slre.h',
        '../../src/foreign/slre/slre.inc_c',
        '../../src/zgossip_engine.inc',
        '../../src/zhash_primes.inc',
        '../../src/zsock_option.inc',
        '../../include/czmq_library.h',
        '../../src/czmq_selftest.c',
        '../../src/czmq_private_selftest.c',
        '../../src/czmq_classes.h'
      ],
      'dependencies': [
        '../../../libzmq/builds/gyp/project.gyp:libzmq',
      ],
      'copies': [
        {
          'destination': '../../src',
          'files': [
              'platform.h'
          ]
        }
      ]
    },
    {
      'target_name': 'zmakecert',
      'type': 'executable',
      'sources': [
        '../../src/zmakecert.c'
      ],
      'dependencies': [
        'libczmq'
      ]
    },
    {
      'target_name': 'zsp',
      'type': 'executable',
      'sources': [
        '../../src/zsp.c'
      ],
      'dependencies': [
        'libczmq'
      ]
    },
    {
      'target_name': 'test-randof',
      'type': 'executable',
      'sources': [
        '../../src/test-randof.c'
      ],
      'dependencies': [
        'libczmq'
      ]
    },
    {
      'target_name': 'czmq_selftest',
      'type': 'executable',
      'sources': [
        '../../src/czmq_selftest.c'
      ],
      'dependencies': [
        'libczmq'
      ]
    }
  ]
}
