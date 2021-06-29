from setuptools import setup


setup(
    name="wsgirpc",
    url="https://github.com/luismsgomes/wsgirpc",
    author="Luís Gomes",
    author_email="luismsgomes@gmail.com",
    version="0.1.0",
    description="Tiny implementation of a WSGI-based RPC server and client",
    package_dir={"": "src"},
    py_modules=["wsgirpc"],
    install_requires=["requests"],
)
