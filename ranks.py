from enum import Enum

class Rank(Enum):
    SSL = 1
    GC3 = 2
    GC2 = 3
    GC1 = 4
    C3 = 5
    C2 = 6
    C1 = 7
    D3 = 8
    D2 = 9
    D1 = 10
    P3 = 11
    P2 = 12
    P1 = 13
    G3 = 14
    G2 = 15
    G1 = 16
    S3 = 17
    S2 = 18
    S1 = 19
    B3 = 20
    B2 = 21
    B1 = 22
    U = 23

rank_emojis = {
    Rank.SSL: '<:01_ssl:874997342909136927>',
    Rank.GC3: '<:02_gc3:874997342942658570>',
    Rank.GC2: '<:03_gc2:874997342951055410>',
    Rank.GC1: '<:04_gc1:874997342993023027>',
    Rank.C3: '<:05_c3:874997343001382973>',
    Rank.C2: '<:06_c2:874997342871371848>',
    Rank.C1: '<:07_c1:874997342762311751>',
    Rank.D3: '<:08_d3:874997343068508210>',
    Rank.D2: '<:09_d2:874997343102074881>',
    Rank.D1: '<:10_d1:874997343039156277>',
    Rank.P3: '<:11_p3:874997343315959898>',
    Rank.P2: '<:12_p2:874997343315959818>',
    Rank.P1: '<:13_p1:874997343232098346>',
    Rank.G3: '<:14_g3:874997343236280340>',
    Rank.G2: '<:15_g2:874997343286599741>',
    Rank.G1: '<:16_g1:874997343060107326>',
    Rank.S3: '<:17_s3:874997343391465512>',
    Rank.S2: '<:18_s2:874997343408226394>',
    Rank.S1: '<:19_s1:874997343299182633>',
    Rank.B3: '<:20_b3:874997343437611018>',
    Rank.B2: '<:21_b2:874997343110443050>',
    Rank.B1: '<:22_b1:874997343387275285>',
    Rank.U: '<:23_u:874997343433408553>'
}

rank_names = {
    Rank.SSL: 'Supersonic Legend',
    Rank.GC1: 'Grand Champion III',
    Rank.GC2: 'Grand Champion II',
    Rank.GC3: 'Grand Champion I',
    Rank.C1: 'Champion III',
    Rank.C2: 'Champion II',
    Rank.C3: 'Champion I',
    Rank.D1: 'Diamond III',
    Rank.D2: 'Diamond II',
    Rank.D3: 'Diamond I',
    Rank.P1: 'Platinum III',
    Rank.P2: 'Platinum II',
    Rank.P3: 'Platinum I',
    Rank.G1: 'Gold III',
    Rank.G2: 'Gold II',
    Rank.G3: 'Gold I',
    Rank.S1: 'Silver III',
    Rank.S2: 'Silver II',
    Rank.S3: 'Silver I',
    Rank.B1: 'Bronze III',
    Rank.B2: 'Bronze II',
    Rank.B3: 'Bronze I',
    Rank.U: 'Unranked'
}