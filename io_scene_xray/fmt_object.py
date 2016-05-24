class Chunks:
    class Object:
        MAIN = 0x7777
        VERSION = 0x0900
        FLAGS = 0x0903
        SURFACES1 = 0x0906
        SURFACES2 = 0x0907
        MESHES = 0x0910
        USERDATA = 0x0912
        MOTIONS = 0x0916
        PARTITIONS0 = 0x0919
        TRANSFORM = 0x0920
        BONES1 = 0x0921
        REVISION = 0x0922
        PARTITIONS1 = 0x0923
        MOTION_REFS = 0x0924
        LOD_REF = 0x0925

    class Mesh:
        class Flags:
            SG_MASK = 0x04
        VERSION = 0x1000
        MESHNAME = 0x1001
        FLAGS = 0x1002
        BBOX = 0x1004
        VERTS = 0x1005
        FACES = 0x1006
        VMAPS0 = 0x1007
        VMREFS = 0x1008
        SFACE = 0x1009
        OPTIONS = 0x1010
        VMAPS2 = 0x1012
        SG = 0x1013

    class Bone:
        VERSION = 0x0001
        DEF = 0x0002
        BIND_POSE = 0x0003
        MATERIAL = 0x0004
        SHAPE = 0x0005
        IK_JOINT = 0x0006
        MASS_PARAMS = 0x0007
        IK_FLAGS = 0x0008
        BREAK_PARAMS = 0x0009
        FRICTION = 0x0010
