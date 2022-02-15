
#
# Python-slip39 -- Ethereum SLIP-39 Account Generation and Recovery
#
# Copyright (c) 2021, Dominion Research & Development Corp.
#
# Python-slip39 is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version. See the LICENSE file at the top of the source tree.
#
# Python-slip39 is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#

#
# HD Wallet Derivation Paths (Standard BIP-44 / Trezor)
#
#     https://wolovim.medium.com/ethereum-201-hd-wallets-11d0c93c87f7
#
# BIP-44 defines the purpose of each depth level:
#    m / purpose’ / coin_type’ / account’ / change / address_index
#
# Use https://iancoleman.io/bip39/ to confirm the derivations
#

# Default group_threshold / required ratios and groups (with varying styles of definition)
GROUP_REQUIRED_RATIO		= 1/2   # default to 1/2 of group members, rounded up
GROUP_THRESHOLD_RATIO		= 1/2   # default to 1/2 of groups, rounded up
GROUPS				= [
    "First1",
    "Second(1/1)",
    "Fam(4)",
    "Frens3/6"
]

FONTS				= dict(
    sans	= 'helvetica',
    mono	= 'courier',
)

#                                  Y      X       Margin
CREDIT_CARD			= (2+1/4, 3+3/8), 1/16
INDEX_CARD			= (3,     5),     1/8   # noqa: E241
BUSINESS_CARD			= (2,     3+1/2), 1/32  # noqa: E241
HALF_LETTER			= (4+1/2, 8),     1/8   # noqa: E241 (actually, 2/letter, 3/legal)
THIRD_LETTER			= (10.5/4,8),     1/8   # noqa: E241 (actually, 3/letter, 4/legal)

# SLIP-39 Mnemonic Card Sizes
CARD				= 'index'
CARD_SIZES			= dict(
    index	= INDEX_CARD,
    credit	= CREDIT_CARD,
    business	= BUSINESS_CARD,
    half	= HALF_LETTER,
    third	= THIRD_LETTER,
)

# Paper Wallet Bill Sizes
WALLET				= 'third'
WALLET_SIZES			= dict(
    third	= THIRD_LETTER,
)

PAGE_MARGIN			= 1/4  # Typical printers cannot print within 1/4" of edge

PAPER				= 'Letter'

BITS				= (128, 256, 512)
BITS_DEFAULT			= 128

MNEM_ROWS_COLS			= {
    20:	( 7, 3),		# 128-bit seed
    33:	(11, 3),		# 256-bit seed
    59:	(12, 5),		# 512-bit seed, eg. from BIP-39 (Unsupported on Trezor hardware wallet)
}


BAUDRATE			= 115200

FILENAME_KEYWORDS		= [ 'name', 'date', 'time', 'crypto', 'path', 'address' ]
FILENAME_FORMAT			= "{name}-{date}+{time}-{crypto}-{address}.pdf"

# Default Crypto accounts (and optional paths) to generate
CRYPTO_PATHS			= [ 'ETH', 'BTC' ]

__o				= "BB"
__h				= "DD"
__f				= "FF"
COLOR				= [
    # Primary
    f"0x{__o}{__o}{__f}",  # Blue
    f"0x{__o}{__f}{__o}",  # Green
    f"0x{__f}{__o}{__o}",  # Red
    # Secondary
    f"0x{__o}{__f}{__f}",  # Cyan,
    f"0x{__f}{__o}{__f}",  # Magenta
    f"0x{__f}{__f}{__o}",  # Yellow
    # Tertiary
    f"0x{__o}{__h}{__f}",  # Ocean
    f"0x{__o}{__f}{__h}",  # Turquoise
    f"0x{__f}{__o}{__h}",  # Red-Magenta
    f"0x{__h}{__o}{__f}",  # Violet
    f"0x{__h}{__f}{__o}",  # Lime
    f"0x{__f}{__h}{__o}",  # Orange
    # Other
    f"0x{__o}{__h}{__h}",  # Light Cyan
    f"0x{__h}{__o}{__h}",  # Light Magenta
    f"0x{__h}{__h}{__o}",  # Light Yellow
    f"0x{__h}{__h}{__h}",  # Light grey,
]
