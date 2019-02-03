#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostContractConan(base.BoostBaseConan):
    name = "boost_contract"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_contract"
    lib_short_names = ["contract"]
    b2_requires = [
        "boost_any",
        "boost_assert",
        "boost_config",
        "boost_core",
        "boost_exception",
        "boost_function",
        "boost_function_types",
        "boost_mpl",
        "boost_optional",
        "boost_preprocessor",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_thread",
        "boost_type_traits",
        "boost_typeof",
        "boost_utility"
    ]
    b2_build_requires = ["boost_system"]
