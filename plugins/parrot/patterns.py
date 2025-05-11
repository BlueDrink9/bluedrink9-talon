from talon import settings

parrot_patterns = {
    "alveolar_click": {
        "sounds": ["alveolar_click"],
        "threshold": {
            ">power": 1,
            ">probability": 0.95,
            # Distinguish against hiss
            "<f2": 4000,
        },
        # "throttle": {"alveolar_click": 0.12, "pop": 0.2},
    },
    "cluck": {
        "sounds": ["cluck"],
        "threshold": {">power": 3, ">probability": 0.90},
        "throttle": {"cluck": 0.1},
    },

    "shush": {
        "sounds": ["shh"],
        "threshold": {">probability": 0.80},
        # "graceperiod": 0.1,
        # "grace_threshold": {">power": 5, ">probability": 0.4},
        "detect_after": 0.1,
        # "detect_after": settings.get('user.hiss_scroll_debounce_time')/1000,
        # "throttle": {"shush": 0.01},
    },

    "hiss": {
        "sounds": ["hiss"],
        "threshold": {">probability": 0.80},
        # "detect_after": settings.get('user.hiss_scroll_debounce_time')/1000,
        "detect_after": 0.1,
        # "graceperiod": 0.1,
        # "grace_threshold": {">power": 5, ">probability": 0.6},
    },

    # like a k sound in the bottom and back of throat
    "throat_kh": {
        "sounds": ["unvoiced unaspirated dorsal velar stop"],
        "threshold": {">power": 5, ">probability": 0.95},
    },

    "kiss": {
        "sounds": ["tenuis labial click"],
        "threshold": {">probability": 0.95},
    },

    "unaspirated_t_stop": {
        "sounds": ["unaspirated voiceless alveolar stop"],
        "threshold": {
            ">probability": 0.95,
            # Distinguish against hiss
            "<f2": 4000,
            "<f0": 500,
        },
    },

    "aspirated_t": {
        "sounds": ["aspirated voiceless alveolar stop"],
        "threshold": {
            ">probability": 0.95,
            # Distinguish against hiss
            "<f2": 4000,
            "<f0": 500,
        },
    },

    "guttural_ach": {
        "sounds": ["voiceless velar fricative"],
        "threshold": {">probability": 0.95},
        "throttle": {
            "cluck": 0.1,
            "voiceless velar fricative": 0.5,
        },
    },

    "voiced_th": {
        "sounds": ["voiced dental fricative"],
        "threshold": {">probability": 0.90},
        "detect_after": 0.1,
    },

    "unvoiced_th": {
        "sounds": ["voiceless dental fricative"],
        "threshold": {">probability": 0.90},
        "detect_after": 0.1,
    },

    # "palate_click": {
    # 	"sounds": ["click_palatal"],
    # 	"threshold": {
    # 		">power": 20,
    # 		">probability": 0.86
    # 	},
    # 	"throttle": {
    # 		"palate_click": 0.12,
    # 		"cluck": 0.15,
    # 		"shush": 0.15
    # 	}
    # },
    # "gluck": {
    # 	"sounds": ["stop_implosive_velar"],
    # 	"threshold": {
    # 		">power": 50,
    # 		">probability": 0.9
    # 	},
    # 	"throttle": {
    # 		"gluck": 0.25
    # 	}
    # },
    # "whistle": {
    # 	"sounds": ["sound_whistle"],
    # 	"threshold": {
    # 		">power": 20,
    # 		">probability": 0.85
    # 	},
    # 	"graceperiod": 0.1,
    # 	"grace_threshold": {
    # 		">power": 15,
    # 		">probability": 0.7
    # 	}
    # },
    # "x": {
    # 	"sounds": ["gutteral_kh"],
    # 	"threshold": {
    # 		">power": 20,
    # 		">probability": 0.85
    # 	}
    # }

}

parrot_patterns["speech"] = {
        "sounds": ["speech"],
        "threshold": {
            ">probability": 0.80,
        # Distinguish against hiss
            "<f2": 4000,
        },
        "throttle": {s: 0.1 for s, _ in parrot_patterns.items()},
}
