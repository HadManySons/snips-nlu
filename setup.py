import io
import os

from setuptools import setup, find_packages

packages = [p for p in find_packages()
            if "tests" not in p and "debug" not in p]

PACKAGE_NAME = "snips_nlu"
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
PACKAGE_PATH = os.path.join(ROOT_PATH, PACKAGE_NAME)
VERSION = "__version__"

with io.open(os.path.join(PACKAGE_PATH, VERSION)) as f:
    version = f.readline().strip()

required = [
    "enum34==1.1.6",
    "numpy==1.14.0",
    "scipy==1.0.0",
    "scikit-learn==0.19.1",
    "sklearn-crfsuite==0.3.6",
    "builtin_entities_ontology==0.5.3",
    "semantic_version==2.6.0",
    "rustling==8.4.1",
    "nlu_utils==0.5.3",
    "num2words==0.5.6"
]

extras_require = {
    "test": [
        "mock==2.0.0",
        "nlu_metrics==0.10.1",
        # "snips_nlu_rust==0.52.0",
        "pylint==1.8.2",
        "coverage==4.4.2"
    ]
}

setup(name=PACKAGE_NAME,
      version=version,
      author="Clement Doumouro, Adrien Ball",
      author_email="clement.doumouro@snips.ai, adrien.ball@snips.ai",
      license="MIT",
      install_requires=required,
      extras_require=extras_require,
      classifiers=[
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
      ],
      packages=packages,
      package_data={
          "": [
              VERSION,
              "snips-nlu-resources/en/*",
              "snips-nlu-resources/fr/*",
              "snips-nlu-resources/es/*",
              "snips-nlu-resources/de/*",
              "snips-nlu-resources/ko/*",
          ]},
      entry_points={
          "console_scripts": [
              "train-engine=cli.cli:main_train_engine",
              "engine-inference=cli.cli:main_engine_inference",
              "cross-val-metrics=cli.cli:main_cross_val_metrics",
              "train-test-metrics=cli.cli:main_train_test_metrics"
          ]
      },
      include_package_data=True,
      zip_safe=False)
