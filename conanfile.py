#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostContractConan(ConanFile):
    name = "boost_contract"
    version = "1.67.0"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["contract"]

    requires = (
        "boost_any/1.67.0@bincrafters/testing",
        "boost_assert/1.67.0@bincrafters/testing",
        "boost_config/1.67.0@bincrafters/testing",
        "boost_core/1.67.0@bincrafters/testing",
        "boost_exception/1.67.0@bincrafters/testing",
        "boost_function/1.67.0@bincrafters/testing",
        "boost_function_types/1.67.0@bincrafters/testing",
        "boost_mpl/1.67.0@bincrafters/testing",
        "boost_optional/1.67.0@bincrafters/testing",
        "boost_package_tools/1.67.0@bincrafters/testing",
        "boost_preprocessor/1.67.0@bincrafters/testing",
        "boost_smart_ptr/1.67.0@bincrafters/testing",
        "boost_static_assert/1.67.0@bincrafters/testing",
        "boost_thread/1.67.0@bincrafters/testing",
        "boost_type_traits/1.67.0@bincrafters/testing",
        "boost_typeof/1.67.0@bincrafters/testing",
        "boost_utility/1.67.0@bincrafters/testing"
    )

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost_contract"
    description = "Please visit http://www.boost.org/doc/libs/1_67_0"
    license = "BSL-1.0"
    short_paths = True
    build_requires = "boost_generator/1.67.0@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()

    # END