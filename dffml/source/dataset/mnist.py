import pathlib

from ..source import Sources
from ..idx3 import IDX3Source
from ..idx1 import IDX1Source
from .base import dataset_source
from ...util.net import cached_download


@dataset_source("mnist.training")
async def mnist_training(
    cache_dir: pathlib.Path = (
        pathlib.Path("~", ".cache", "dffml", "datasets", "mnist")
        .expanduser()
        .resolve()
    )
):
    """
    MNIST handwritten digits dataset (training set).

    Note: This requires network access to download the dataset from
    http://yann.lecun.com/exdb/mnist/
    """
    # Download features
    features_path = await cached_download(
        "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz",
        cache_dir / "training_original_features.gz",
        "1bf45877962fd391f7abb20534a30fd2203d0865309fec5f87d576dbdbefdcb16adb49220afc22a0f3478359d229449c",
        protocol_allowlist=["http://"],
    )
    # Download labels
    labels_path = await cached_download(
        "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz",
        cache_dir / "training_original_labels.gz",
        "b13a73e8bdcea05b2271a6b9f5b75cc9e5fc35e7caf42a2d34ec74e3b68db2cbb27eb2ce2fcd17c3a7c3e20e0c64c7f3d",
        protocol_allowlist=["http://"],
    )
    # Create a source object which is acctualy two sources combined.
    # This will expose the seperate features and labels files we downloaded as a
    # single source.
    yield Sources(
        IDX3Source(filename=features_path, feature="image"),
        IDX1Source(filename=labels_path, feature="label"),
    )
