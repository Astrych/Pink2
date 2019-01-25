# Copyright (c) 2013-2016 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.


AM_LDFLAGS = $(PTHREAD_CFLAGS) $(LIBTOOL_LDFLAGS) $(HARDENED_LDFLAGS) $(GPROF_LDFLAGS) $(SANITIZER_LDFLAGS)
AM_CXXFLAGS = $(DEBUG_CXXFLAGS) $(HARDENED_CXXFLAGS) $(WARN_CXXFLAGS) $(NOWARN_CXXFLAGS) $(ERROR_CXXFLAGS) $(GPROF_CXXFLAGS) $(SANITIZER_CXXFLAGS)
AM_CPPFLAGS = $(DEBUG_CPPFLAGS) $(HARDENED_CPPFLAGS)
AM_LIBTOOLFLAGS = --preserve-dup-deps
EXTRA_LIBRARIES =


PINKCOIN_INCLUDES=-I$(builddir) $(BDB_CPPFLAGS) $(BOOST_CPPFLAGS) $(LEVELDB_CPPFLAGS) $(CRYPTO_CFLAGS) $(SSL_CFLAGS)

LIBPINKCOINQT=qt/libpinkcoinqt.a

bin_PROGRAMS =
noinst_PROGRAMS =

if BUILD_PINKCOIND
  bin_PROGRAMS += pinkcoind
endif

.PHONY: FORCE check-symbols check-security
# pinkcoin core #
PINKCOIN_CORE_H = \
  alert.h \
  addrman.h \
  base58.h \
  bignum.h \
  checkpoints.h \
  compat.h \
  coincontrol.h \
  sync.h \
  util.h \
  uint256.h \
  kernel.h \
  scrypt.h \
  pbkdf2.h \
  serialize.h \
  smessage.h \
  main.h \
  miner.h \
  net.h \
  key.h \
  db.h \
  txdb.h \
  walletdb.h \
  stakedb.h \
  script.h \
  stealth.h \
  init.h \
  mruset.h \
  json/json_spirit_writer_template.h \
  json/json_spirit_writer.h \
  json/json_spirit_value.h \
  json/json_spirit_utils.h \
  json/json_spirit_stream_reader.h \
  json/json_spirit_reader_template.h \
  json/json_spirit_reader.h \
  json/json_spirit_error_position.h \
  json/json_spirit.h \
  wallet.h \
  keystore.h \
  bitcoinrpc.h \
  crypter.h \
  protocol.h \
  allocators.h \
  ui_interface.h \
  version.h \
  netbase.h \
  clientversion.h \
  threadsafety.h \
  txdb-leveldb.h

obj/build.h: FORCE
	@$(MKDIR_P) $(builddir)/obj
	@$(top_srcdir)/share/genbuild.sh "$(abs_top_builddir)/src/obj/build.h" \
	  "$(abs_top_srcdir)"

pinkcoin_server_CPPFLAGS = $(AM_CPPFLAGS) $(PINKCOIN_INCLUDES) $(MINIUPNPC_CPPFLAGS) $(EVENT_CFLAGS) $(EVENT_PTHREADS_CFLAGS)
pinkcoin_server_CXXFLAGS = $(AM_CXXFLAGS) $(PIE_FLAGS)
pinkcoin_server_SOURCES = \
  alert.cpp \
  version.cpp \
  sync.cpp \
  smessage.cpp \
  util.cpp \
  netbase.cpp \
  key.cpp \
  script.cpp \
  main.cpp \
  miner.cpp \
  init.cpp \
  net.cpp \
  checkpoints.cpp \
  addrman.cpp \
  db.cpp \
  walletdb.cpp \
  stakedb.cpp \
  wallet.cpp \
  keystore.cpp \
  bitcoinrpc.cpp \
  rpcdump.cpp \
  rpcnet.cpp \
  rpcmining.cpp \
  rpcwallet.cpp \
  rpcblockchain.cpp \
  rpcrawtransaction.cpp \
  rpcsmessage.cpp \
  crypter.cpp \
  protocol.cpp \
  noui.cpp \
  kernel.cpp \
  scrypt-arm.S \
  scrypt-x86.S \
  scrypt-x86_64.S \
  scrypt.cpp \
  pbkdf2.cpp \
  stealth.cpp \
  txdb-leveldb.cpp \
  $(PINKCOIN_CORE_H)


# pinkcoind binary #
pinkcoind_SOURCES = $(pinkcoin_server_SOURCES)
pinkcoind_CPPFLAGS = $(pinkcoin_server_CPPFLAGS)
pinkcoind_CXXFLAGS = $(pinkcoin_server_CXXFLAGS)
pinkcoind_LDFLAGS = $(RELDFLAGS) $(AM_LDFLAGS) $(LIBTOOL_APP_LDFLAGS)

pinkcoind_LDADD = $(LIBLEVELDB) $(LIBMEMENV)
pinkcoind_LDADD += $(BOOST_LIBS) $(BDB_LIBS) $(SSL_LIBS) $(CRYPTO_LIBS) $(MINIUPNPC_LIBS) $(EVENT_PTHREADS_LIBS) $(EVENT_LIBS)


CLEANFILES = $(EXTRA_LIBRARIES)

CLEANFILES += *.gcda *.gcno
CLEANFILES += obj/build.h

clean-local:
	-rm -f leveldb/*/*.gcda leveldb/*/*.gcno leveldb/helpers/memenv/*.gcda leveldb/helpers/memenv/*.gcno
	-rm -f config.h
	-rm -rf test/__pycache__

.rc.o:
	@test -f $(WINDRES)
	## FIXME: How to get the appropriate modulename_CPPFLAGS in here?
	$(AM_V_GEN) $(WINDRES) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(CPPFLAGS) -DWINDRES_PREPROC -i $< -o $@

check-security: $(bin_PROGRAMS)
if HARDEN
	@echo "Checking binary security..."
	$(AM_V_at) READELF=$(READELF) OBJDUMP=$(OBJDUMP) $(top_srcdir)/contrib/devtools/security-check.py < $(bin_PROGRAMS)
endif

include Makefile.leveldb.include

# include Makefile.qt.include
