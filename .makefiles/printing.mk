# Printing functions
ESC    := \033[
RESET  := $(ESC)0m
BOLD   := $(ESC)1m
FG_RED := $(ESC)31m
FG_YEL := $(ESC)33m
FG_BLU := $(ESC)34m
BG_BLU := $(ESC)44m

define coloring
	printf '$(1)$(BOLD)[$(2)]$(RESET) $(3) $(1)$(BOLD)[$(2)]$(RESET)\n'
endef

define pinfo
	$(call coloring,$(FG_BLU),INFO,$(1))
endef

define pwarn
	$(call coloring,$(FG_YEL),WARN,$(1))
endef

define perror
	$(call coloring,$(FG_RED),ERROR,$(1))
endef
