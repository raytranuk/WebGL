#!/usr/bin/env python

# Copyright (c) 2019 The Khronos Group Inc.
# Use of this source code is governed by an MIT-style license that can be
# found in the LICENSE.txt file.

"""
  Generator for textureformat* tests.
  This file needs to be run in its folder.
"""

import sys

_DO_NOT_EDIT_WARNING = """<!--

This file is auto-generated from textureformat_test_generator.py
DO NOT EDIT!

-->

"""

_HTML_TEMPLATE = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>WebGL Texture Specification Tests</title>
<link rel="stylesheet" href="../../../../resources/js-test-style.css"/>
<script src="../../../../js/js-test-pre.js"></script>
<script src="../../../../js/webgl-test-utils.js"></script>

<script src="../../../../closure-library/closure/goog/base.js"></script>
<script src="../../../deqp-deps.js"></script>
<script>goog.require('functional.gles3.es3fTextureFormatTests');</script>
</head>
<body>
<div id="description"></div>
<div id="console"></div>
<canvas id="canvas" width="300" height="300"> </canvas>
<script>
var wtu = WebGLTestUtils;
var gl = wtu.create3DContext('canvas', null, 2);

functional.gles3.es3fTextureFormatTests.run(gl, [%(start)s, %(end)s]);
</script>
</body>
</html>
"""

_GROUPS = [
    'unsized_2d',
    'unsized_2d_array',
    'unsized_3d',
    'sized_color_2d_pot_00',
    'sized_color_2d_pot_01',
    'sized_color_2d_pot_02',
    'sized_color_2d_pot_03',
    'sized_color_2d_npot_00',
    'sized_color_2d_npot_01',
    'sized_color_2d_npot_02',
    'sized_color_2d_npot_03',
    'sized_color_cube_pot_00',
    'sized_color_cube_pot_01',
    'sized_color_cube_pot_02',
    'sized_color_cube_pot_03',
    'sized_color_cube_npot_00',
    'sized_color_cube_npot_01',
    'sized_color_cube_npot_02',
    'sized_color_cube_npot_03',
    'sized_color_2d_array_pot_00',
    'sized_color_2d_array_pot_01',
    'sized_color_2d_array_pot_02',
    'sized_color_2d_array_pot_03',
    'sized_color_2d_array_npot_00',
    'sized_color_2d_array_npot_01',
    'sized_color_2d_array_npot_02',
    'sized_color_2d_array_npot_03',
    'sized_color_3d_pot_00',
    'sized_color_3d_pot_01',
    'sized_color_3d_pot_02',
    'sized_color_3d_pot_03',
    'sized_color_3d_npot_00',
    'sized_color_3d_npot_01',
    'sized_color_3d_npot_02',
    'sized_color_3d_npot_03',
    'sized_depth_stencil',
    'compressed_2d',
    'compressed_cube',
]

def GenerateFilename(group):
  """Generate test filename."""
  filename = group
  filename += ".html"
  return filename

def WriteTest(filename, start, end):
  """Write one test."""
  file = open(filename, "wb")
  file.write(_DO_NOT_EDIT_WARNING)
  file.write(_HTML_TEMPLATE % {
    'start': start,
    'end': end
  })
  file.close

def GenerateTests():
  """Generate all tests."""
  filelist = []
  for ii in range(len(_GROUPS)):
    filename = GenerateFilename(_GROUPS[ii])
    filelist.append(filename)
    WriteTest(filename, ii, ii + 1)
  return filelist

def GenerateTestList(filelist):
  file = open("00_test_list.txt", "wb")
  file.write('\n'.join(filelist))
  file.close

def main(argv):
  """This is the main function."""
  filelist = GenerateTests()
  GenerateTestList(filelist)

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
