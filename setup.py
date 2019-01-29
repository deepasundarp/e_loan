from setuptools import setup

setup(
    name="e_loan",
    description="Energy Loan Package",
    keywords=["smart grid", "renewables", "balancing", "energy market", "flexibility", "demand-response"],
    version="0.1",
    install_requires=[
        "pandas",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    packages=["e_loan"],
    include_package_data=True,
    # license="Apache",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
    ],
    long_description="""\
Energy Loan package performs the role of a central market for the product of energy loan based flexibility service. 
It accepts the bids and asks collected from the Buyers and Sellers in the form of '.csv' file in the specified format. 
After allocations being made, it reports back as a DataFrame, which can be communicated back to stakeholders.
""",
)
