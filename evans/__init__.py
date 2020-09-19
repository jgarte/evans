"""
Evans API

The personal Abjad library of Gregory Rowland Evans.
"""
from .commands import (
    Command,
    HandlerCommand,
    RhythmCommand,
    attach,
    call,
    detach,
    replace,
)
from .consort import (
    LogicalTieCollection,
    RatioPartsExpression,
    TimespanCollection,
    TimespanSimultaneity,
)
from .handlers import (
    ArticulationHandler,
    BendHandler,
    BisbigliandoHandler,
    ClefHandler,
    DynamicHandler,
    GettatoHandler,
    GlissandoHandler,
    GraceHandler,
    NoteheadHandler,
    PitchHandler,
    RhythmHandler,
    SlurHandler,
    TempoSpannerHandler,
    TextSpanHandler,
    TrillHandler,
)
from .metmod import (
    calculate_metric_modulation,
    calculate_tempo_modulated_duration,
    compare_speed,
    metric_modulation,
    mixed_number,
)
from .pitch import (
    combination_multiples,
    combination_tones,
    herz_combination_tone_ratios,
    relative_ratios,
    return_cent_markup,
    return_vertical_moment_ties,
    to_nearest_eighth_tone,
    to_nearest_quarter_tone,
    to_nearest_sixth_tone,
    to_nearest_third_tone,
    to_nearest_twelfth_tone,
    tonnetz,
    tune_to_ratio,
)
from .rtm import (
    RTMMaker,
    funnel_inner_tree_to_x,
    funnel_tree_to_x,
    nested_list_to_rtm,
    rotate_tree,
)
from .segmentmaker import NoteheadBracketMaker, SegmentMaker, beam_meter
from .sequence import (
    CyclicList,
    MarkovChain,
    add_sequences,
    cyc,
    derive_added_sequences,
    derive_multiplied_sequences,
    e_bonacci_cycle,
    e_dovan_cycle,
    feigenbaum_bifurcations,
    flatten,
    grouper,
    guerrero_morales,
    harmonic_series,
    hexagonal_sequence,
    josephus,
    lindenmayer,
    mirror,
    mod,
    multiple_sequence,
    multiply_all,
    multiply_sequences,
    n_bonacci_cycle,
    normalize_sum,
    normalize_to_indices,
    orbits,
    perm,
    pitch_warp,
    prime_sequence,
    prism_sequence,
    random_walk,
    recaman_sequence,
    reciprocal,
    reduce_mod,
    reproportion_chord,
    reproportion_chromatic_decimals,
    reproportion_harmonics,
    reproportion_scale,
    rotate,
    warp,
)
from .timespan import (
    SilentTimespan,
    TimespanMaker,
    TimespanSpecifier,
    add_silences_to_timespan_dict,
    add_silences_to_timespan_lists,
    add_silent_timespans,
    collect_offsets,
    human_sorted_keys,
    intercalate_silences,
    make_showable_list,
    make_split_list,
    sorted_keys,
    talea_timespans,
    to_digit,
)

__all__ = [
    "ArticulationHandler",
    "BendHandler",
    "BisbigliandoHandler",
    "ClefHandler",
    "Command",
    "CyclicList",
    "DynamicHandler",
    "GettatoHandler",
    "GlissandoHandler",
    "GraceHandler",
    "HandlerCommand",
    "LogicalTieCollection",
    "MarkovChain",
    "NoteheadBracketMaker",
    "NoteheadHandler",
    "PitchHandler",
    "RTMMaker",
    "RatioPartsExpression",
    "RhythmCommand",
    "RhythmHandler",
    "SegmentMaker",
    "SilentTimespan",
    "SlurHandler",
    "TempoSpannerHandler",
    "TextSpanHandler",
    "TimespanCollection",
    "TimespanMaker",
    "TimespanSimultaneity",
    "TimespanSpecifier",
    "TrillHandler",
    "add_sequences",
    "add_silences_to_timespan_dict",
    "add_silences_to_timespan_lists",
    "add_silent_timespans",
    "attach",
    "beam_meter",
    "calculate_metric_modulation",
    "calculate_tempo_modulated_duration",
    "call",
    "collect_offsets",
    "combination_multiples",
    "combination_tones",
    "compare_speed",
    "cyc",
    "derive_added_sequences",
    "derive_multiplied_sequences",
    "detach",
    "e_bonacci_cycle",
    "e_dovan_cycle",
    "feigenbaum_bifurcations",
    "flatten",
    "funnel_inner_tree_to_x",
    "funnel_tree_to_x",
    "grouper",
    "guerrero_morales",
    "harmonic_series",
    "herz_combination_tone_ratios",
    "hexagonal_sequence",
    "human_sorted_keys",
    "intercalate_silences",
    "josephus",
    "lindenmayer",
    "make_showable_list",
    "make_split_list",
    "metric_modulation",
    "mirror",
    "mixed_number",
    "mod",
    "multiple_sequence",
    "multiply_all",
    "multiply_sequences",
    "n_bonacci_cycle",
    "nested_list_to_rtm",
    "normalize_sum",
    "normalize_to_indices",
    "orbits",
    "perm",
    "pitch_warp",
    "prime_sequence",
    "prism_sequence",
    "random_walk",
    "recaman_sequence",
    "reciprocal",
    "reduce_mod",
    "relative_ratios",
    "replace",
    "reproportion_chord",
    "reproportion_chromatic_decimals",
    "reproportion_harmonics",
    "reproportion_scale",
    "return_cent_markup",
    "return_vertical_moment_ties",
    "rotate",
    "rotate_tree",
    "sorted_keys",
    "talea_timespans",
    "to_digit",
    "to_nearest_eighth_tone",
    "to_nearest_quarter_tone",
    "to_nearest_sixth_tone",
    "to_nearest_third_tone",
    "to_nearest_twelfth_tone",
    "tonnetz",
    "tune_to_ratio",
    "warp",
]
