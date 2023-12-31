from enum import Enum

# https://bulbapedia.bulbagarden.net/wiki/List_of_locations_by_index_number_(Generation_III)
# Map Banks and IDs were OCR scanned from Advance Map ROM hacking tool, it is possible there are mistakes


class MapFRLG(Enum):
    UNKNOWN = (0, 0)
    CELADON_DEPT = (0, 1)
    CELADON_DEPT_A = (0, 2)
    CELADON_DEPT_B = (0, 3)
    CELADON_DEPT_C = (0, 4)

    VIRIDIAN_FOREST = (1, 0)
    MT_MOON = (1, 1)
    MT_MOON_A = (1, 2)
    MT_MOON_B = (1, 3)
    SS_ANNE = (1, 4)
    SS_ANNE_A = (1, 5)
    SS_ANNE_B = (1, 6)
    SS_ANNE_C = (1, 7)
    SS_ANNE_D = (1, 8)
    SS_ANNE_E = (1, 9)
    SS_ANNE_F = (1, 10)
    SS_ANNE_G = (1, 11)
    SS_ANNE_H = (1, 12)
    SS_ANNE_I = (1, 13)
    SS_ANNE_J = (1, 14)
    SS_ANNE_K = (1, 15)
    SS_ANNE_L = (1, 16)
    SS_ANNE_M = (1, 17)
    SS_ANNE_N = (1, 18)
    SS_ANNE_O = (1, 19)
    SS_ANNE_P = (1, 20)
    SS_ANNE_Q = (1, 21)
    SS_ANNE_R = (1, 22)
    SS_ANNE_S = (1, 23)
    SS_ANNE_T = (1, 24)
    SS_ANNE_U = (1, 25)
    SS_ANNE_V = (1, 26)
    SS_ANNE_W = (1, 27)
    SS_ANNE_X = (1, 28)
    SS_ANNE_Y = (1, 29)
    UNDERGROUND_PATH = (1, 30)
    UNDERGROUND_PATH_A = (1, 31)
    UNDERGROUND_PATH_B = (1, 32)
    UNDERGROUND_PATH_C = (1, 33)
    UNDERGROUND_PATH_D = (1, 34)
    UNDERGROUND_PATH_E = (1, 35)
    DIGLETTS_CAVE = (1, 36)
    DIGLETTS_CAVE_A = (1, 37)
    DIGLETTS_CAVE_B = (1, 38)
    VICTORY_ROAD = (1, 39)
    VICTORY_ROAD_A = (1, 40)
    VICTORY_ROAD_B = (1, 41)
    ROCKET_HIDEOUT = (1, 42)
    ROCKET_HIDEOUT_A = (1, 43)
    ROCKET_HIDEOUT_B = (1, 44)
    ROCKET_HIDEOUT_C = (1, 45)
    ROCKET_HIDEOUT_D = (1, 46)
    SILPH_CO = (1, 47)
    SILPH_CO_A = (1, 48)
    SILPH_CO_B = (1, 49)
    SILPH_CO_C = (1, 50)
    SILPH_CO_D = (1, 51)
    SILPH_CO_E = (1, 52)
    SILPH_CO_F = (1, 53)
    SILPH_CO_G = (1, 54)
    SILPH_CO_H = (1, 55)
    SILPH_CO_I = (1, 56)
    SILPH_CO_J = (1, 57)
    SILPH_CO_K = (1, 58)
    POKEMON_MANSION = (1, 59)
    POKEMON_MANSION_A = (1, 60)
    POKEMON_MANSION_B = (1, 61)
    POKEMON_MANSION_C = (1, 62)
    SAFARI_ZONE = (1, 63)
    SAFARI_ZONE_A = (1, 64)
    SAFARI_ZONE_B = (1, 65)
    SAFARI_ZONE_C = (1, 66)
    SAFARI_ZONE_D = (1, 67)
    SAFARI_ZONE_E = (1, 68)
    SAFARI_ZONE_F = (1, 69)
    SAFARI_ZONE_G = (1, 70)
    SAFARI_ZONE_H = (1, 71)
    CERULEAN_CAVE = (1, 72)
    CERULEAN_CAVE_A = (1, 73)
    CERULEAN_CAVE_B = (1, 74)
    POKEMON_LEAGUE = (1, 75)
    POKEMON_LEAGUE_A = (1, 76)
    POKEMON_LEAGUE_B = (1, 77)
    POKEMON_LEAGUE_C = (1, 78)
    POKEMON_LEAGUE_D = (1, 79)
    POKEMON_LEAGUE_E = (1, 80)
    ROCK_TUNNEL = (1, 81)
    ROCK_TUNNEL_A = (1, 82)
    SEAFOAM_ISLANDS = (1, 83)
    SEAFOAM_ISLANDS_A = (1, 84)
    SEAFOAM_ISLANDS_B = (1, 85)
    SEAFOAM_ISLANDS_C = (1, 86)
    SEAFOAM_ISLANDS_D = (1, 87)
    POKEMON_TOWER = (1, 88)
    POKEMON_TOWER_A = (1, 89)
    POKEMON_TOWER_B = (1, 90)
    POKEMON_TOWER_C = (1, 91)
    POKEMON_TOWER_D = (1, 92)
    POKEMON_TOWER_E = (1, 93)
    POKEMON_TOWER_F = (1, 94)
    POWER_PLANT = (1, 95)
    MT_EMBER = (1, 96)
    MT_EMBER_A = (1, 97)
    MT_EMBER_B = (1, 98)
    MT_EMBER_C = (1, 99)
    MT_EMBER_D = (1, 100)
    MT_EMBER_E = (1, 101)
    MT_EMBER_F = (1, 102)
    MT_EMBER_G = (1, 103)
    MT_EMBER_H = (1, 104)
    MT_EMBER_I = (1, 105)
    MT_EMBER_J = (1, 106)
    MT_EMBER_K = (1, 107)
    MT_EMBER_L = (1, 108)
    BERRY_FOREST = (1, 109)
    ICEFALL_CAVE = (1, 110)
    ICEFALL_CAVE_A = (1, 111)
    ICEFALL_CAVE_B = (1, 112)
    ICEFALL_CAVE_C = (1, 113)
    ROCKET_WAREHOUSE = (1, 114)
    DOTTED_HOLE = (1, 115)
    DOTTED_HOLE_A = (1, 116)
    DOTTED_HOLE_B = (1, 117)
    DOTTED_HOLE_C = (1, 118)
    DOTTED_HOLE_D = (1, 119)
    DOTTED_HOLE_E = (1, 120)
    PATTERN_BUSH = (1, 121)
    ALTERING_CAVE = (1, 122)

    TRAINER_TOWER = (2, 1)
    TRAINER_TOWER_A = (2, 2)
    TRAINER_TOWER_B = (2, 3)
    TRAINER_TOWER_C = (2, 4)
    TRAINER_TOWER_D = (2, 5)
    TRAINER_TOWER_E = (2, 6)
    TRAINER_TOWER_F = (2, 7)
    TRAINER_TOWER_G = (2, 8)
    TRAINER_TOWER_H = (2, 9)
    TRAINER_TOWER_I = (2, 10)
    TRAINER_TOWER_J = (2, 11)
    LOST_CAVE = (2, 12)
    LOST_CAVE_A = (2, 13)
    LOST_CAVE_B = (2, 14)
    LOST_CAVE_C = (2, 15)
    LOST_CAVE_D = (2, 16)
    LOST_CAVE_E = (2, 17)
    LOST_CAVE_F = (2, 18)
    LOST_CAVE_G = (2, 19)
    LOST_CAVE_H = (2, 20)
    LOST_CAVE_I = (2, 21)
    LOST_CAVE_J = (2, 22)
    LOST_CAVE_K = (2, 23)
    LOST_CAVE_L = (2, 24)
    LOST_CAVE_M = (2, 25)
    LOST_CAVE_N = (2, 26)
    MONEAN_CHAMBER = (2, 27)
    LIPTOO_CHAMBER = (2, 28)
    WEEPTH_CHAMBER = (2, 29)
    DILFORD_CHAMBER = (2, 30)
    SCUFIB_CHAMBER = (2, 31)
    RIXY_CHAMBER = (2, 32)
    VIAPOIS_CHAMBER = (2, 33)
    THREE_ISLE_PATH = (2, 34)
    TANOBY_KEY = (2, 35)
    NAVEL_ROCK = (2, 36)
    NAVEL_ROCK_A = (2, 37)
    NAVEL_ROCK_B = (2, 38)
    NAVEL_ROCK_C = (2, 39)
    NAVEL_ROCK_D = (2, 40)
    NAVEL_ROCK_E = (2, 41)
    NAVEL_ROCK_F = (2, 42)
    NAVEL_ROCK_G = (2, 43)
    NAVEL_ROCK_H = (2, 44)
    NAVEL_ROCK_I = (2, 45)
    NAVEL_ROCK_J = (2, 46)
    NAVEL_ROCK_K = (2, 47)
    NAVEL_ROCK_L = (2, 48)
    NAVEL_ROCK_M = (2, 49)
    NAVEL_ROCK_N = (2, 50)
    NAVEL_ROCK_O = (2, 51)
    NAVEL_ROCK_P = (2, 52)
    NAVEL_ROCK_Q = (2, 53)
    NAVEL_ROCK_R = (2, 54)
    NAVEL_ROCK_S = (2, 55)
    BIRTH_ISLAND = (2, 56)
    EMBER_SPA = (2, 57)
    BIRTH_ISLAND_A = (2, 58)
    NAVEL_ROCK_T = (2, 59)

    PALLET_TOWN = (3, 0)
    VIRIDIAN_CITY = (3, 1)
    PEWTER_CITY = (3, 2)
    CERULEAN_CITY = (3, 3)
    LAVENDER_TOWN = (3, 4)
    VERMILION_CITY = (3, 5)
    CELADON_CITY = (3, 6)
    FUCHSIA_CITY = (3, 7)
    CINNABAR_ISLAND = (3, 8)
    INDIGO_PLATEAU = (3, 9)
    SAFFRON_CITY = (3, 10)
    SAFFRON_CITY_A = (3, 11)
    ONE_ISLAND = (3, 12)
    TWO_ISLAND = (3, 13)
    THREE_ISLAND = (3, 14)
    FOUR_ISLAND = (3, 15)
    FIVE_ISLAND = (3, 16)
    SEVEN_ISLAND = (3, 17)
    SIX_ISLAND = (3, 18)
    ROUTE_1 = (3, 19)
    ROUTE_2 = (3, 20)
    ROUTE_3 = (3, 21)
    ROUTE_4 = (3, 22)
    ROUTE_5 = (3, 23)
    ROUTE_6 = (3, 24)
    ROUTE_7 = (3, 25)
    ROUTE_8 = (3, 26)
    ROUTE_9 = (3, 27)
    ROUTE_10 = (3, 28)
    ROUTE_11 = (3, 29)
    ROUTE_12 = (3, 30)
    ROUTE_13 = (3, 31)
    ROUTE_14 = (3, 32)
    ROUTE_15 = (3, 33)
    ROUTE_16 = (3, 34)
    ROUTE_17 = (3, 35)
    ROUTE_18 = (3, 36)
    ROUTE_19 = (3, 37)
    ROUTE_20 = (3, 38)
    ROUTE_21 = (3, 39)
    ROUTE_21_A = (3, 40)
    ROUTE_22 = (3, 41)
    ROUTE_23 = (3, 42)
    ROUTE_24 = (3, 43)
    ROUTE_25 = (3, 44)
    KINDLE_ROAD = (3, 45)
    TREASURE_BEACH = (3, 46)
    CAPE_BRINK = (3, 47)
    BOND_BRIDGE = (3, 48)
    THREE_ISLE_PORT = (3, 49)
    SEVII_ISLE_6 = (3, 50)
    SEVII_ISLE_7 = (3, 51)
    SEVII_ISLE_8 = (3, 52)
    SEVII_ISLE_9 = (3, 53)
    RESORT_GORGEOUS = (3, 54)
    WATER_LABYRINTH = (3, 55)
    FIVE_ISLE_MEADOW = (3, 56)
    MEMORIAL_PILLAR = (3, 57)
    OUTCAST_ISLAND = (3, 58)
    GREEN_PATH = (3, 59)
    WATER_PATH = (3, 60)
    RUIN_VALLEY = (3, 61)
    TRAINER_TOWER_K = (3, 62)
    CANYON_ENTRANCE = (3, 63)
    SEVAULT_CANYON = (3, 64)
    TANOBY_RUINS = (3, 65)

    PALLET_TOWN_A = (4, 0)
    PALLET_TOWN_B = (4, 1)
    PALLET_TOWN_C = (4, 2)
    PALLET_TOWN_D = (4, 3)

    VIRIDIAN_CITY_A = (5, 0)
    VIRIDIAN_CITY_B = (5, 1)
    VIRIDIAN_CITY_C = (5, 2)
    VIRIDIAN_CITY_D = (5, 3)
    VIRIDIAN_CITY_E = (5, 4)
    VIRIDIAN_CITY_F = (5, 5)

    PEWTER_CITY_A = (6, 0)
    PEWTER_CITY_B = (6, 1)
    PEWTER_CITY_C = (6, 2)
    PEWTER_CITY_D = (6, 3)
    PEWTER_CITY_E = (6, 4)
    PEWTER_CITY_F = (6, 5)
    PEWTER_CITY_G = (6, 6)
    PEWTER_CITY_H = (6, 7)

    CERULEAN_CITY_A = (7, 0)
    CERULEAN_CITY_B = (7, 1)
    CERULEAN_CITY_C = (7, 2)
    CERULEAN_CITY_D = (7, 3)
    CERULEAN_CITY_E = (7, 4)
    CERULEAN_CITY_F = (7, 5)
    CERULEAN_CITY_G = (7, 6)
    CERULEAN_CITY_H = (7, 7)
    CERULEAN_CITY_I = (7, 8)
    CERULEAN_CITY_J = (7, 9)

    LAVENDER_TOWN_A = (8, 0)
    LAVENDER_TOWN_B = (8, 1)
    LAVENDER_TOWN_C = (8, 2)
    LAVENDER_TOWN_D = (8, 3)
    LAVENDER_TOWN_E = (8, 4)
    LAVENDER_TOWN_F = (8, 5)

    VERMILION_CITY_A = (9, 0)
    VERMILION_CITY_B = (9, 1)
    VERMILION_CITY_C = (9, 2)
    VERMILION_CITY_D = (9, 3)
    VERMILION_CITY_E = (9, 4)
    VERMILION_CITY_F = (9, 5)
    VERMILION_CITY_G = (9, 6)
    VERMILION_CITY_H = (9, 7)

    CELADON_CITY_A = (10, 0)
    CELADON_CITY_B = (10, 1)
    CELADON_CITY_C = (10, 2)
    CELADON_CITY_D = (10, 3)
    CELADON_CITY_E = (10, 4)
    CELADON_CITY_F = (10, 5)
    CELADON_CITY_G = (10, 6)
    CELADON_CITY_H = (10, 7)
    CELADON_CITY_I = (10, 8)
    CELADON_CITY_J = (10, 9)
    CELADON_CITY_K = (10, 10)
    CELADON_CITY_L = (10, 11)
    CELADON_CITY_M = (10, 12)
    CELADON_CITY_N = (10, 13)
    CELADON_CITY_O = (10, 14)
    CELADON_CITY_P = (10, 15)
    CELADON_CITY_Q = (10, 16)
    CELADON_CITY_R = (10, 17)
    CELADON_CITY_S = (10, 18)
    CELADON_CITY_T = (10, 19)

    FUCHSIA_CITY_A = (11, 0)
    FUCHSIA_CITY_B = (11, 1)
    FUCHSIA_CITY_C = (11, 2)
    FUCHSIA_CITY_D = (11, 3)
    FUCHSIA_CITY_E = (11, 4)
    FUCHSIA_CITY_F = (11, 5)
    FUCHSIA_CITY_G = (11, 6)
    FUCHSIA_CITY_H = (11, 7)
    FUCHSIA_CITY_I = (11, 8)
    FUCHSIA_CITY_J = (11, 9)

    CINNABAR_ISLAND_A = (12, 0)
    CINNABAR_ISLAND_B = (12, 1)
    CINNABAR_ISLAND_C = (12, 2)
    CINNABAR_ISLAND_D = (12, 3)
    CINNABAR_ISLAND_E = (12, 4)
    CINNABAR_ISLAND_F = (12, 5)
    CINNABAR_ISLAND_G = (12, 6)
    CINNABAR_ISLAND_H = (12, 7)

    INDIGO_PLATEAU_A = (13, 0)
    INDIGO_PLATEAU_B = (13, 1)

    SAFFRON_CITY_B = (14, 0)
    SAFFRON_CITY_C = (14, 1)
    SAFFRON_CITY_D = (14, 2)
    SAFFRON_CITY_E = (14, 3)
    SAFFRON_CITY_F = (14, 4)
    SAFFRON_CITY_G = (14, 5)
    SAFFRON_CITY_H = (14, 6)
    SAFFRON_CITY_I = (14, 7)
    SAFFRON_CITY_J = (14, 8)
    SAFFRON_CITY_K = (14, 9)

    ROUTE_2_A = (15, 0)
    ROUTE_2_B = (15, 1)
    ROUTE_2_C = (15, 2)
    ROUTE_2_D = (15, 3)

    ROUTE_4_A = (16, 0)
    ROUTE_4_B = (16, 1)

    ROUTE_5_A = (17, 0)
    ROUTE_5_B = (17, 1)

    ROUTE_6_A = (18, 0)
    ROUTE_6_B = (18, 1)

    ROUTE_7_A = (19, 0)

    ROUTE_8_A = (20, 0)

    ROUTE_10_A = (21, 0)
    ROUTE_10_B = (21, 1)

    ROUTE_11_A = (22, 0)
    ROUTE_11_B = (22, 1)

    ROUTE_12_A = (23, 0)
    ROUTE_12_B = (23, 1)
    ROUTE_12_C = (23, 2)

    ROUTE_15_A = (24, 0)
    ROUTE_15_B = (24, 1)

    ROUTE_16_A = (25, 0)
    ROUTE_16_B = (25, 1)
    ROUTE_16_C = (25, 2)

    ROUTE_18_A = (26, 0)
    ROUTE_18_B = (26, 1)

    ROUTE_19_A = (27, 0)

    ROUTE_22_A = (28, 0)

    ROUTE_23_A = (29, 0)

    ROUTE_25_A = (30, 0)

    SEVEN_ISLAND_A = (31, 0)
    SEVEN_ISLAND_B = (31, 1)
    SEVEN_ISLAND_C = (31, 2)
    SEVEN_ISLAND_D = (31, 3)
    SEVEN_ISLAND_E = (31, 4)
    SEVEN_ISLAND_F = (31, 5)
    SEVEN_ISLAND_G = (31, 6)

    ONE_ISLAND_A = (32, 0)
    ONE_ISLAND_B = (32, 1)
    ONE_ISLAND_C = (32, 2)
    ONE_ISLAND_D = (32, 3)
    ONE_ISLAND_E = (32, 4)

    TWO_ISLAND_A = (33, 0)
    TWO_ISLAND_B = (33, 1)
    TWO_ISLAND_C = (33, 2)
    TWO_ISLAND_D = (33, 3)
    TWO_ISLAND_E = (33, 4)

    THREE_ISLAND_A = (34, 0)
    THREE_ISLAND_B = (34, 1)
    THREE_ISLAND_C = (34, 2)
    THREE_ISLAND_D = (34, 3)
    THREE_ISLAND_E = (34, 4)
    THREE_ISLAND_F = (34, 5)
    THREE_ISLAND_G = (34, 6)
    THREE_ISLAND_H = (34, 7)

    FOUR_ISLAND_A = (35, 0)
    FOUR_ISLAND_B = (35, 1)
    FOUR_ISLAND_C = (35, 2)
    FOUR_ISLAND_D = (35, 3)
    FOUR_ISLAND_E = (35, 4)
    FOUR_ISLAND_F = (35, 5)
    FOUR_ISLAND_G = (35, 6)
    FOUR_ISLAND_H = (35, 7)

    FIVE_ISLAND_A = (36, 0)
    FIVE_ISLAND_B = (36, 1)
    FIVE_ISLAND_C = (36, 2)
    FIVE_ISLAND_D = (36, 3)
    FIVE_ISLAND_E = (36, 4)

    SIX_ISLAND_A = (37, 0)
    SIX_ISLAND_B = (37, 1)
    SIX_ISLAND_C = (37, 2)
    SIX_ISLAND_D = (37, 3)
    SIX_ISLAND_E = (37, 4)

    THREE_ISLE_PORT_A = (38, 0)

    RESORT_GORGEOUS_A = (39, 0)

    CAPE_BRINK_A = (40, 0)

    WATER_PATH_A = (41, 0)
    WATER_PATH_B = (41, 1)

    SEVAULT_CANYON_A = (42, 0)


class MapRSE(Enum):
    PETALBURG_CITY = (0, 0)
    SLATEPORT_CITY = (0, 1)
    MAUVILLE_CITY = (0, 2)
    RUSTBORO_CITY = (0, 3)
    FORTREE_CITY = (0, 4)
    LILYCOVE_CITY = (0, 5)
    MOSSDEEP_CITY = (0, 6)
    SOOTOPOLIS_CITY = (0, 7)
    EVER_GRANDE_CITY = (0, 8)
    LITTLEROOT_TOWN = (0, 9)
    OLDALE_TOWN = (0, 10)
    DEWFORD_TOWN = (0, 11)
    LAVARIDGE_TOWN = (0, 12)
    FALLARBOR_TOWN = (0, 13)
    VERDANTURF_TOWN = (0, 14)
    PACIFIDLOG_TOWN = (0, 15)
    ROUTE_101 = (0, 16)
    ROUTE_102 = (0, 17)
    ROUTE_103 = (0, 18)
    ROUTE_104 = (0, 19)
    ROUTE_105 = (0, 20)
    ROUTE_106 = (0, 21)
    ROUTE_107 = (0, 22)
    ROUTE_108 = (0, 23)
    ROUTE_109 = (0, 24)
    ROUTE_110 = (0, 25)
    ROUTE_111 = (0, 26)
    ROUTE_112 = (0, 27)
    ROUTE_113 = (0, 28)
    ROUTE_114 = (0, 29)
    ROUTE_115 = (0, 30)
    ROUTE_116 = (0, 31)
    ROUTE_117 = (0, 32)
    ROUTE_118 = (0, 33)
    ROUTE_119 = (0, 34)
    ROUTE_120 = (0, 35)
    ROUTE_121 = (0, 36)
    ROUTE_122 = (0, 37)
    ROUTE_123 = (0, 38)
    ROUTE_124 = (0, 39)
    ROUTE_125 = (0, 40)
    ROUTE_126 = (0, 41)
    ROUTE_127 = (0, 42)
    ROUTE_128 = (0, 43)
    ROUTE_129 = (0, 44)
    ROUTE_130 = (0, 45)
    ROUTE_131 = (0, 46)
    ROUTE_132 = (0, 47)
    ROUTE_133 = (0, 48)
    ROUTE_134 = (0, 49)
    UNDERWATER = (0, 50)
    UNDERWATER_A = (0, 51)
    UNDERWATER_B = (0, 52)
    UNDERWATER_C = (0, 53)
    UNDERWATER_D = (0, 54)
    UNDERWATER_E = (0, 55)
    UNDERWATER_F = (0, 56)

    LITTLEROOT_TOWN_A = (1, 0)
    LITTLEROOT_TOWN_B = (1, 1)
    LITTLEROOT_TOWN_C = (1, 2)
    LITTLEROOT_TOWN_D = (1, 3)
    LITTLEROOT_TOWN_E = (1, 4)  # Prof. Birch's Lab

    OLDALE_TOWN_A = (2, 0)
    OLDALE_TOWN_B = (2, 1)
    OLDALE_TOWN_C = (2, 2)
    OLDALE_TOWN_D = (2, 3)
    OLDALE_TOWN_E = (2, 4)

    DEWFORD_TOWN_A = (3, 0)
    DEWFORD_TOWN_B = (3, 1)
    DEWFORD_TOWN_C = (3, 2)
    DEWFORD_TOWN_D = (3, 3)
    DEWFORD_TOWN_E = (3, 4)
    DEWFORD_TOWN_F = (3, 5)

    LAVARIDGE_TOWN_A = (4, 0)
    LAVARIDGE_TOWN_B = (4, 1)
    LAVARIDGE_TOWN_C = (4, 2)
    LAVARIDGE_TOWN_D = (4, 3)
    LAVARIDGE_TOWN_E = (4, 4)
    LAVARIDGE_TOWN_F = (4, 5)
    LAVARIDGE_TOWN_G = (4, 6)

    FALLARBOR_TOWN_A = (5, 0)
    FALLARBOR_TOWN_B = (5, 1)
    FALLARBOR_TOWN_C = (5, 2)
    FALLARBOR_TOWN_D = (5, 3)
    FALLARBOR_TOWN_E = (5, 4)
    FALLARBOR_TOWN_F = (5, 5)
    FALLARBOR_TOWN_G = (5, 6)
    FALLARBOR_TOWN_H = (5, 7)

    VERDANTURF_TOWN_A = (6, 0)
    VERDANTURF_TOWN_B = (6, 1)
    VERDANTURF_TOWN_C = (6, 2)
    VERDANTURF_TOWN_D = (6, 3)
    VERDANTURF_TOWN_E = (6, 4)
    VERDANTURF_TOWN_F = (6, 5)
    VERDANTURF_TOWN_G = (6, 6)
    VERDANTURF_TOWN_H = (6, 7)
    VERDANTURF_TOWN_I = (6, 8)

    PACIFIDLOG_TOWN_A = (7, 0)
    PACIFIDLOG_TOWN_B = (7, 1)
    PACIFIDLOG_TOWN_C = (7, 2)
    PACIFIDLOG_TOWN_D = (7, 3)
    PACIFIDLOG_TOWN_E = (7, 4)
    PACIFIDLOG_TOWN_F = (7, 5)
    PACIFIDLOG_TOWN_G = (7, 6)

    PETALBURG_CITY_A = (8, 0)
    PETALBURG_CITY_B = (8, 1)
    PETALBURG_CITY_C = (8, 2)
    PETALBURG_CITY_D = (8, 3)
    PETALBURG_CITY_E = (8, 4)
    PETALBURG_CITY_F = (8, 5)
    PETALBURG_CITY_G = (8, 6)

    SLATEPORT_CITY_A = (9, 0)
    SLATEPORT_CITY_B = (9, 1)
    SLATEPORT_CITY_C = (9, 2)
    SLATEPORT_CITY_D = (9, 3)
    SLATEPORT_CITY_E = (9, 4)
    SLATEPORT_CITY_F = (9, 5)
    SLATEPORT_CITY_G = (9, 6)
    SLATEPORT_CITY_H = (9, 7)
    SLATEPORT_CITY_I = (9, 8)
    SLATEPORT_CITY_J = (9, 9)
    SLATEPORT_CITY_K = (9, 10)
    SLATEPORT_CITY_L = (9, 11)
    SLATEPORT_CITY_M = (9, 13)

    MAUVILLE_CITY_A = (10, 0)
    MAUVILLE_CITY_B = (10, 1)
    MAUVILLE_CITY_C = (10, 2)
    MAUVILLE_CITY_D = (10, 3)
    MAUVILLE_CITY_E = (10, 4)
    MAUVILLE_CITY_F = (10, 5)
    MAUVILLE_CITY_G = (10, 6)
    MAUVILLE_CITY_H = (10, 7)

    RUSTBORO_CITY_A = (11, 0)
    RUSTBORO_CITY_B = (11, 1)  # Devon Corp. 2F
    RUSTBORO_CITY_C = (11, 2)
    RUSTBORO_CITY_D = (11, 3)
    RUSTBORO_CITY_E = (11, 4)
    RUSTBORO_CITY_F = (11, 5)
    RUSTBORO_CITY_G = (11, 6)
    RUSTBORO_CITY_H = (11, 7)
    RUSTBORO_CITY_I = (11, 8)
    RUSTBORO_CITY_J = (11, 9)
    RUSTBORO_CITY_K = (11, 10)
    RUSTBORO_CITY_L = (11, 11)
    RUSTBORO_CITY_M = (11, 12)
    RUSTBORO_CITY_N = (11, 13)
    RUSTBORO_CITY_O = (11, 14)
    RUSTBORO_CITY_P = (11, 15)
    RUSTBORO_CITY_Q = (11, 16)

    FORTREE_CITY_A = (12, 0)
    FORTREE_CITY_B = (12, 1)
    FORTREE_CITY_C = (12, 2)
    FORTREE_CITY_D = (12, 3)
    FORTREE_CITY_E = (12, 4)
    FORTREE_CITY_F = (12, 5)
    FORTREE_CITY_G = (12, 6)
    FORTREE_CITY_H = (12, 7)
    FORTREE_CITY_I = (12, 8)
    FORTREE_CITY_J = (12, 9)

    LILYCOVE_CITY_A = (13, 0)
    LILYCOVE_CITY_B = (13, 1)
    LILYCOVE_CITY_C = (13, 2)
    LILYCOVE_CITY_D = (13, 3)
    LILYCOVE_CITY_E = (13, 4)
    LILYCOVE_CITY_F = (13, 5)
    LILYCOVE_CITY_G = (13, 6)
    LILYCOVE_CITY_H = (13, 7)
    LILYCOVE_CITY_I = (13, 8)
    LILYCOVE_CITY_J = (13, 9)
    LILYCOVE_CITY_K = (13, 10)
    LILYCOVE_CITY_L = (13, 11)
    LILYCOVE_CITY_M = (13, 12)
    LILYCOVE_CITY_N = (13, 13)
    LILYCOVE_CITY_O = (13, 14)
    LILYCOVE_CITY_P = (13, 15)
    LILYCOVE_CITY_Q = (13, 16)
    LILYCOVE_CITY_R = (13, 17)
    LILYCOVE_CITY_S = (13, 18)
    LILYCOVE_CITY_T = (13, 19)
    LILYCOVE_CITY_U = (13, 20)
    LILYCOVE_CITY_V = (13, 21)
    LILYCOVE_CITY_W = (13, 22)

    MOSSDEEP_CITY_A = (14, 0)
    MOSSDEEP_CITY_B = (14, 1)
    MOSSDEEP_CITY_C = (14, 2)
    MOSSDEEP_CITY_D = (14, 3)
    MOSSDEEP_CITY_E = (14, 4)
    MOSSDEEP_CITY_F = (14, 5)
    MOSSDEEP_CITY_G = (14, 6)
    MOSSDEEP_CITY_H = (14, 7)
    MOSSDEEP_CITY_I = (14, 8)
    MOSSDEEP_CITY_J = (14, 9)
    MOSSDEEP_CITY_K = (14, 11)
    MOSSDEEP_CITY_L = (14, 12)

    SOOTOPOLIS_CITY_A = (15, 0)
    SOOTOPOLIS_CITY_B = (15, 1)
    SOOTOPOLIS_CITY_C = (15, 2)
    SOOTOPOLIS_CITY_D = (15, 3)
    SOOTOPOLIS_CITY_E = (15, 4)
    SOOTOPOLIS_CITY_F = (15, 5)
    SOOTOPOLIS_CITY_G = (15, 6)
    SOOTOPOLIS_CITY_H = (15, 7)
    SOOTOPOLIS_CITY_I = (15, 8)
    SOOTOPOLIS_CITY_J = (15, 9)
    SOOTOPOLIS_CITY_K = (15, 10)
    SOOTOPOLIS_CITY_L = (15, 11)
    SOOTOPOLIS_CITY_M = (15, 12)
    SOOTOPOLIS_CITY_N = (15, 13)
    SOOTOPOLIS_CITY_O = (15, 14)

    EVER_GRANDE_CITY_A = (16, 0)
    EVER_GRANDE_CITY_B = (16, 1)
    EVER_GRANDE_CITY_C = (16, 2)
    EVER_GRANDE_CITY_D = (16, 3)
    EVER_GRANDE_CITY_E = (16, 4)
    EVER_GRANDE_CITY_F = (16, 5)
    EVER_GRANDE_CITY_G = (16, 6)
    EVER_GRANDE_CITY_H = (16, 7)
    EVER_GRANDE_CITY_I = (16, 8)
    EVER_GRANDE_CITY_J = (16, 9)
    EVER_GRANDE_CITY_K = (16, 10)
    EVER_GRANDE_CITY_L = (16, 11)
    EVER_GRANDE_CITY_M = (16, 12)
    EVER_GRANDE_CITY_N = (16, 13)
    EVER_GRANDE_CITY_O = (16, 14)

    ROUTE_104_A = (17, 0)
    ROUTE_104_B = (17, 1)

    ROUTE_11_A = (18, 0)
    ROUTE_11_B = (18, 1)

    ROUTE_112_A = (19, 0)
    MT_CHIMNEY = (19, 1)

    ROUTE_114_A = (20, 0)
    ROUTE_114_B = (20, 1)
    ROUTE_114_C = (20, 2)

    ROUTE_116_A = (21, 0)

    ROUTE_117_A = (22, 0)

    ROUTE_121_A = (23, 0)

    METEOR_FALLS = (24, 0)
    METEOR_FALLS_A = (24, 1)
    METEOR_FALLS_B = (24, 2)
    METEOR_FALLS_C = (24, 3)
    RUSTURF_TUNNEL = (24, 4)
    UNDERWATER_H = (24, 5)
    DESERT_RUINS = (24, 6)  # Regirock Cave
    GRANITE_CAVE = (24, 7)
    GRANITE_CAVE_A = (24, 8)
    GRANITE_CAVE_B = (24, 9)
    GRANITE_CAVE_C = (24, 10)
    PETALBURG_WOODS = (24, 11)
    MT_CHIMNEY_A = (24, 12)
    JAGGED_PASS = (24, 13)
    FIERY_PATH = (24, 14)
    MT_PYRE = (24, 15)
    MT_PYRE_A = (24, 16)
    MT_PYRE_B = (24, 17)
    MT_PYRE_C = (24, 18)
    MT_PYRE_D = (24, 19)
    MT_PYRE_E = (24, 20)
    MT_PYRE_F = (24, 21)
    MT_PYRE_G = (24, 22)
    AQUA_HIDEOUT = (24, 23)
    AQUA_HIDEOUT_A = (24, 24)
    AQUA_HIDEOUT_B = (24, 25)
    UNDERWATER_I = (24, 26)
    SEAFLOOR_CAVERN = (24, 27)
    SEAFLOOR_CAVERN_A = (24, 28)
    SEAFLOOR_CAVERN_B = (24, 29)
    SEAFLOOR_CAVERN_C = (24, 30)
    SEAFLOOR_CAVERN_D = (24, 31)
    SEAFLOOR_CAVERN_E = (24, 32)
    SEAFLOOR_CAVERN_F = (24, 33)
    SEAFLOOR_CAVERN_G = (24, 34)
    SEAFLOOR_CAVERN_H = (24, 35)
    SEAFLOOR_CAVERN_I = (24, 36)
    CAVE_OF_ORIGIN = (24, 37)
    CAVE_OF_ORIGIN_A = (24, 38)
    CAVE_OF_ORIGIN_B = (24, 39)
    CAVE_OF_ORIGIN_C = (24, 40)
    CAVE_OF_ORIGIN_D = (24, 41)
    CAVE_OF_ORIGIN_E = (24, 42)
    VICTORY_ROAD = (24, 43)
    VICTORY_ROAD_A = (24, 44)
    VICTORY_ROAD_B = (24, 45)
    SHOAL_CAVE = (24, 46)
    SHOAL_CAVE_A = (24, 47)
    SHOAL_CAVE_B = (24, 48)
    SHOAL_CAVE_C = (24, 49)
    SHOAL_CAVE_D = (24, 50)
    SHOAL_CAVE_E = (24, 51)
    NEW_MAUVILLE = (24, 52)
    NEW_MAUVILLE_A = (24, 53)
    ABANDONED_SHIP = (24, 54)
    ABANDONED_SHIP_A = (24, 55)
    ABANDONED_SHIP_B = (24, 56)
    ABANDONED_SHIP_C = (24, 57)
    ABANDONED_SHIP_D = (24, 58)
    ABANDONED_SHIP_E = (24, 59)
    ABANDONED_SHIP_F = (24, 60)
    ABANDONED_SHIP_G = (24, 61)
    ABANDONED_SHIP_H = (24, 62)
    ABANDONED_SHIP_I = (24, 63)
    ABANDONED_SHIP_J = (24, 64)
    ABANDONED_SHIP_K = (24, 65)
    ABANDONED_SHIP_L = (24, 66)
    ISLAND_CAVE = (24, 67)  # Regice Cave
    ANCIENT_TOMB = (24, 68)  # Registeel Cave
    UNDERWATER_J = (24, 69)
    UNDERWATER_K = (24, 70)
    SEALED_CHAMBER = (24, 71)
    SEALED_CHAMBER_A = (24, 72)
    SCORCHED_SLAB = (24, 73)
    AQUA_HIDEOUT_C = (24, 74)
    AQUA_HIDEOUT_D = (24, 75)
    AQUA_HIDEOUT_E = (24, 76)
    SKY_PILLAR = (24, 77)
    SKY_PILLAR_A = (24, 78)
    SKY_PILLAR_B = (24, 79)
    SKY_PILLAR_C = (24, 80)
    SKY_PILLAR_D = (24, 81)
    SKY_PILLAR_E = (24, 82)
    SHOAL_CAVE_F = (24, 83)
    SKY_PILLAR_F = (24, 84)  # Sky Pillar 5F
    SKY_PILLAR_G = (24, 85)  # Top of Sky Pillar (Rayquaza)
    MAGMA_HIDEOUT = (24, 86)
    MAGMA_HIDEOUT_A = (24, 87)
    MAGMA_HIDEOUT_B = (24, 88)
    MAGMA_HIDEOUT_C = (24, 89)
    MAGMA_HIDEOUT_D = (24, 90)
    MAGMA_HIDEOUT_E = (24, 91)
    MAGMA_HIDEOUT_F = (24, 92)
    MAGMA_HIDEOUT_G = (24, 93)
    MIRAGE_TOWER = (24, 94)
    MIRAGE_TOWER_A = (24, 95)
    MIRAGE_TOWER_B = (24, 96)
    MIRAGE_TOWER_C = (24, 97)
    DESERT_UNDERPASS = (24, 98)
    ARTISAN_CAVE = (24, 99)
    ARTISAN_CAVE_A = (24, 100)
    UNDERWATER_L = (24, 101)
    MARINE_CAVE = (24, 102)  # Outside Kyogre Cave
    MARINE_CAVE_A = (24, 103)  # Kyogre Cave
    TERRA_CAVE = (24, 104)  # Outside Groudon Cave
    TERRA_CAVE_A = (24, 105)  # Groudon Cave
    ALTERING_CAVE = (24, 106)
    METEOR_FALLS_D = (24, 107)

    SECRET_BASE = (25, 0)
    SECRET_BASE_A = (25, 1)
    SECRET_BASE_B = (25, 2)
    SECRET_BASE_C = (25, 3)
    SECRET_BASE_D = (25, 4)
    SECRET_BASE_E = (25, 5)
    SECRET_BASE_F = (25, 6)
    SECRET_BASE_G = (25, 7)
    SECRET_BASE_H = (25, 8)
    SECRET_BASE_I = (25, 9)
    SECRET_BASE_J = (25, 10)
    SECRET_BASE_K = (25, 11)
    SECRET_BASE_L = (25, 12)
    SECRET_BASE_M = (25, 13)
    SECRET_BASE_N = (25, 14)
    SECRET_BASE_O = (25, 15)
    SECRET_BASE_P = (25, 16)
    SECRET_BASE_Q = (25, 17)
    SECRET_BASE_R = (25, 18)
    SECRET_BASE_S = (25, 19)
    SECRET_BASE_T = (25, 20)
    SECRET_BASE_U = (25, 21)
    SECRET_BASE_V = (25, 22)
    SECRET_BASE_W = (25, 23)
    UNKNOWN = (25, 24)
    UNKNOWN_A = (25, 25)
    UNKNOWN_B = (25, 26)
    UNKNOWN_C = (25, 27)
    UNKNOWN_D = (25, 28)
    UNKNOWN_E = (25, 29)
    UNKNOWN_F = (25, 30)
    UNKNOWN_G = (25, 31)
    UNKNOWN_H = (25, 32)
    UNKNOWN_I = (25, 33)
    UNKNOWN_J = (25, 34)
    UNKNOWN_K = (25, 35)
    UNKNOWN_L = (25, 36)
    UNKNOWN_M = (25, 37)
    UNKNOWN_N = (25, 38)
    UNKNOWN_O = (25, 39)
    INSIDE_OF_TRUCK = (25, 40)
    UNKNOWN_P = (25, 41)
    UNKNOWN_Q = (25, 42)
    UNKNOWN_R = (25, 43)
    UNKNOWN_S = (25, 44)
    UNKNOWN_T = (25, 45)
    UNKNOWN_U = (25, 46)
    UNKNOWN_V = (25, 47)
    UNKNOWN_W = (25, 48)
    UNKNOWN_X = (25, 49)
    UNKNOWN_Y = (25, 50)
    UNKNOWN_Z = (25, 51)
    UNKNOWN_AA = (25, 52)
    UNKNOWN_AB = (25, 53)
    UNKNOWN_AC = (25, 54)
    UNKNOWN_AD = (25, 55)
    UNKNOWN_AE = (25, 56)
    UNKNOWN_AF = (25, 57)
    UNKNOWN_AG = (25, 58)
    UNKNOWN_AH = (25, 59)
    UNKNOWN_AI = (25, 60)

    SAFARI_ZONE = (26, 0)
    SAFARI_ZONE_A = (26, 1)
    SAFARI_ZONE_B = (26, 2)
    SAFARI_ZONE_C = (26, 3)
    BATTLE_FRONTIER = (26, 4)
    BATTLE_FRONTIER_A = (26, 5)
    BATTLE_FRONTIER_B = (26, 6)
    BATTLE_FRONTIER_C = (26, 7)
    BATTLE_FRONTIER_D = (26, 8)
    SOUTHERN_ISLAND = (26, 9)  # Roamer island (Latios/Latias)
    SOUTHERN_ISLAND_A = (26, 10)  # Roamer island (Latios/Latias)
    SAFARI_ZONE_D = (26, 11)
    SAFARI_ZONE_E = (26, 12)
    SAFARI_ZONE_F = (26, 13)
    BATTLE_FRONTIER_E = (26, 14)
    BATTLE_FRONTIER_F = (26, 15)
    BATTLE_FRONTIER_G = (26, 16)
    BATTLE_FRONTIER_H = (26, 17)
    BATTLE_FRONTIER_I = (26, 18)
    BATTLE_FRONTIER_J = (26, 19)
    BATTLE_FRONTIER_K = (26, 20)
    BATTLE_FRONTIER_L = (26, 21)
    BATTLE_FRONTIER_M = (26, 22)
    BATTLE_FRONTIER_N = (26, 23)
    BATTLE_FRONTIER_O = (26, 24)
    BATTLE_FRONTIER_P = (26, 25)
    BATTLE_FRONTIER_Q = (26, 26)
    BATTLE_FRONTIER_R = (26, 27)
    BATTLE_FRONTIER_S = (26, 28)
    BATTLE_FRONTIER_T = (26, 29)
    BATTLE_FRONTIER_U = (26, 30)
    BATTLE_FRONTIER_V = (26, 31)
    BATTLE_FRONTIER_W = (26, 32)
    BATTLE_FRONTIER_X = (26, 33)
    BATTLE_FRONTIER_Y = (26, 34)
    BATTLE_FRONTIER_Z = (26, 35)
    BATTLE_FRONTIER_AA = (26, 36)
    BATTLE_FRONTIER_AB = (26, 37)
    BATTLE_FRONTIER_AC = (26, 39)
    BATTLE_FRONTIER_AD = (26, 39)
    BATTLE_FRONTIER_AE = (26, 40)
    BATTLE_FRONTIER_AF = (26, 41)
    BATTLE_FRONTIER_AG = (26, 42)
    BATTLE_FRONTIER_AH = (26, 43)
    BATTLE_FRONTIER_AI = (26, 44)
    BATTLE_FRONTIER_AJ = (26, 45)
    BATTLE_FRONTIER_AK = (26, 46)
    BATTLE_FRONTIER_AL = (26, 47)
    BATTLE_FRONTIER_AM = (26, 48)
    BATTLE_FRONTIER_AN = (26, 49)
    BATTLE_FRONTIER_AO = (26, 50)
    BATTLE_FRONTIER_AP = (26, 51)
    BATTLE_FRONTIER_AQ = (26, 52)
    BATTLE_FRONTIER_AR = (26, 53)
    BATTLE_FRONTIER_AS = (26, 54)
    BATTLE_FRONTIER_AT = (26, 55)
    FARAWAY_ISLAND = (26, 56)  # Mew
    FARAWAY_ISLAND_A = (26, 57)  # Mew
    BIRTH_ISLAND = (26, 58)  # Deoxys
    BIRTH_ISLAND_A = (26, 59)  # Deoxys
    TRAINER_HILL = (26, 60)
    TRAINER_HILL_A = (26, 61)
    TRAINER_HILL_B = (26, 62)
    TRAINER_HILL_C = (26, 63)
    TRAINER_HILL_D = (26, 64)
    TRAINER_HILL_E = (26, 65)
    NAVEL_ROCK = (26, 66)
    NAVEL_ROCK_A = (26, 67)
    NAVEL_ROCK_B = (26, 68)
    NAVEL_ROCK_C = (26, 69)
    NAVEL_ROCK_D = (26, 70)
    NAVEL_ROCK_E = (26, 71)
    NAVEL_ROCK_F = (26, 72)
    NAVEL_ROCK_G = (26, 73)
    NAVEL_ROCK_H = (26, 74)  # Ho-Oh
    NAVEL_ROCK_I = (26, 75)  # Ho-Oh
    NAVEL_ROCK_J = (26, 76)
    NAVEL_ROCK_K = (26, 77)
    NAVEL_ROCK_L = (26, 78)
    NAVEL_ROCK_M = (26, 79)
    NAVEL_ROCK_N = (26, 80)
    NAVEL_ROCK_O = (26, 81)
    NAVEL_ROCK_P = (26, 82)
    NAVEL_ROCK_Q = (26, 83)
    NAVEL_ROCK_R = (26, 84)
    NAVEL_ROCK_S = (26, 85)
    NAVEL_ROCK_T = (26, 86)  # Lugia
    NAVEL_ROCK_U = (26, 87)  # Lugia
    TRAINER_HILL_F = (26, 88)

    ROUTE_104_C = (27, 0)
    ROUTE_104_D = (27, 1)

    ROUTE_109_A = (28, 0)

    ROUTE_110_A = (29, 0)
    ROUTE_110_B = (29, 1)
    ROUTE_110_C = (29, 2)
    ROUTE_110_D = (29, 3)
    ROUTE_110_E = (29, 4)
    ROUTE_110_F = (29, 5)
    ROUTE_110_G = (29, 6)
    ROUTE_110_H = (29, 7)
    ROUTE_110_I = (29, 8)
    ROUTE_110_J = (29, 9)
    ROUTE_110_K = (29, 10)
    ROUTE_110_L = (29, 11)
    ROUTE_110_M = (29, 12)

    ROUTE_113_A = (30, 0)

    ROUTE_123_A = (31, 0)

    ROUTE_119_A = (32, 0)
    ROUTE_119_B = (32, 1)  # Weather Institute 2F
    ROUTE_119_C = (32, 2)

    ROUTE_124_A = (33, 0)
