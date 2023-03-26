from feature_encoder import AtomFeatureEncoder, BondFeatureEncoder
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from configuration.training import atoms, bonds


def atom_feature_encoder():
    return AtomFeatureEncoder(allowed_feature_sets=atoms())


def bond_feature_encoder():
    return BondFeatureEncoder(allowed_feature_sets=bonds())