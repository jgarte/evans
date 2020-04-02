\version "2.19.84"  %! abjad.LilyPondFile._get_format_pieces()
\language "english" %! abjad.LilyPondFile._get_format_pieces()

#(set! paper-alist (cons '("newsize" . (cons (* 10 in) (* 30 in))) paper-alist))
#(set-default-paper-size "newsize")
#(set-global-staff-size 10)

\header { %! abjad.LilyPondFile._get_formatted_blocks()
    tagline = ##f
} %! abjad.LilyPondFile._get_formatted_blocks()

\layout {}

\paper {}

\score { %! abjad.LilyPondFile._get_formatted_blocks()
    \new Score
    <<
        \new StaffGroup
        <<
            \new StaffGroup
            <<
                \new Staff
                {
                    \time 3/4
                    c'4
                    f'4
                    g'4
                    g'4
                    c'4
                    d'4
                    f'4
                    bf'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    g'4
                    f'4
                    f'4
                    c'4
                    bf'4
                    g'4
                    d'4
                    c'4
                }
                \new Staff
                {
                    g'4
                    f'4
                    c'4
                    d'4
                    c'4
                    g'4
                    c'4
                    bf'4
                    f'4
                }
                \new Staff
                {
                    f'4
                    g'4
                    c'4
                    bf'4
                    c'4
                    f'4
                    c'4
                    d'4
                    g'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    d'4
                    g'4
                    bf'4
                    c'4
                    f'4
                    f'4
                    g'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    bf'4
                    f'4
                    d'4
                    c'4
                    g'4
                    g'4
                    f'4
                    c'4
                }
                \new Staff
                {
                    g'4
                    d'4
                    c'4
                    f'4
                    c'4
                    bf'4
                    c'4
                    g'4
                    f'4
                }
                \new Staff
                {
                    f'4
                    bf'4
                    c'4
                    g'4
                    c'4
                    d'4
                    c'4
                    f'4
                    g'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    f'4
                    bf'4
                    g'4
                    c'4
                    f'4
                    d'4
                    g'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    g'4
                    d'4
                    f'4
                    c'4
                    g'4
                    bf'4
                    f'4
                    c'4
                }
                \new Staff
                {
                    bf'4
                    f'4
                    c'4
                    f'4
                    c'4
                    g'4
                    c'4
                    g'4
                    d'4
                }
                \new Staff
                {
                    d'4
                    g'4
                    c'4
                    g'4
                    c'4
                    f'4
                    c'4
                    f'4
                    bf'4
                }
            >>
        >>
        \new StaffGroup
        <<
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    d'4
                    af'4
                    bf'4
                    c'4
                    fs'4
                    e'4
                    fs'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    bf'4
                    e'4
                    d'4
                    c'4
                    fs'4
                    af'4
                    fs'4
                    c'4
                }
                \new Staff
                {
                    af'4
                    d'4
                    c'4
                    fs'4
                    c'4
                    bf'4
                    c'4
                    fs'4
                    e'4
                }
                \new Staff
                {
                    e'4
                    bf'4
                    c'4
                    fs'4
                    c'4
                    d'4
                    c'4
                    fs'4
                    af'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    fs'4
                    bf'4
                    fs'4
                    c'4
                    e'4
                    d'4
                    af'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    fs'4
                    d'4
                    fs'4
                    c'4
                    af'4
                    bf'4
                    e'4
                    c'4
                }
                \new Staff
                {
                    bf'4
                    fs'4
                    c'4
                    e'4
                    c'4
                    fs'4
                    c'4
                    af'4
                    d'4
                }
                \new Staff
                {
                    d'4
                    fs'4
                    c'4
                    af'4
                    c'4
                    fs'4
                    c'4
                    e'4
                    bf'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    e'4
                    fs'4
                    af'4
                    c'4
                    d'4
                    fs'4
                    bf'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    af'4
                    fs'4
                    e'4
                    c'4
                    bf'4
                    fs'4
                    d'4
                    c'4
                }
                \new Staff
                {
                    fs'4
                    e'4
                    c'4
                    d'4
                    c'4
                    af'4
                    c'4
                    bf'4
                    fs'4
                }
                \new Staff
                {
                    fs'4
                    af'4
                    c'4
                    bf'4
                    c'4
                    e'4
                    c'4
                    d'4
                    fs'4
                }
            >>
        >>
        \new StaffGroup
        <<
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    fs'4
                    a'4
                    fs'4
                    c'4
                    ef'4
                    ef'4
                    a'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    fs'4
                    ef'4
                    fs'4
                    c'4
                    a'4
                    a'4
                    ef'4
                    c'4
                }
                \new Staff
                {
                    a'4
                    fs'4
                    c'4
                    ef'4
                    c'4
                    fs'4
                    c'4
                    a'4
                    ef'4
                }
                \new Staff
                {
                    ef'4
                    fs'4
                    c'4
                    a'4
                    c'4
                    fs'4
                    c'4
                    ef'4
                    a'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    ef'4
                    fs'4
                    a'4
                    c'4
                    ef'4
                    fs'4
                    a'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    a'4
                    fs'4
                    ef'4
                    c'4
                    a'4
                    fs'4
                    ef'4
                    c'4
                }
                \new Staff
                {
                    fs'4
                    ef'4
                    c'4
                    ef'4
                    c'4
                    a'4
                    c'4
                    a'4
                    fs'4
                }
                \new Staff
                {
                    fs'4
                    a'4
                    c'4
                    a'4
                    c'4
                    ef'4
                    c'4
                    ef'4
                    fs'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    ef'4
                    a'4
                    a'4
                    c'4
                    fs'4
                    ef'4
                    fs'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    a'4
                    ef'4
                    ef'4
                    c'4
                    fs'4
                    a'4
                    fs'4
                    c'4
                }
                \new Staff
                {
                    a'4
                    ef'4
                    c'4
                    fs'4
                    c'4
                    a'4
                    c'4
                    fs'4
                    ef'4
                }
                \new Staff
                {
                    ef'4
                    a'4
                    c'4
                    fs'4
                    c'4
                    ef'4
                    c'4
                    fs'4
                    a'4
                }
            >>
        >>
        \new StaffGroup
        <<
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    ef'4
                    bf'4
                    a'4
                    c'4
                    g'4
                    d'4
                    f'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    a'4
                    d'4
                    ef'4
                    c'4
                    f'4
                    bf'4
                    g'4
                    c'4
                }
                \new Staff
                {
                    bf'4
                    ef'4
                    c'4
                    g'4
                    c'4
                    a'4
                    c'4
                    f'4
                    d'4
                }
                \new Staff
                {
                    d'4
                    a'4
                    c'4
                    f'4
                    c'4
                    ef'4
                    c'4
                    g'4
                    bf'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    g'4
                    a'4
                    f'4
                    c'4
                    d'4
                    ef'4
                    bf'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    f'4
                    ef'4
                    g'4
                    c'4
                    bf'4
                    a'4
                    d'4
                    c'4
                }
                \new Staff
                {
                    a'4
                    g'4
                    c'4
                    d'4
                    c'4
                    f'4
                    c'4
                    bf'4
                    ef'4
                }
                \new Staff
                {
                    ef'4
                    f'4
                    c'4
                    bf'4
                    c'4
                    g'4
                    c'4
                    d'4
                    a'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    d'4
                    f'4
                    bf'4
                    c'4
                    ef'4
                    g'4
                    a'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    bf'4
                    g'4
                    d'4
                    c'4
                    a'4
                    f'4
                    ef'4
                    c'4
                }
                \new Staff
                {
                    f'4
                    d'4
                    c'4
                    ef'4
                    c'4
                    bf'4
                    c'4
                    a'4
                    g'4
                }
                \new Staff
                {
                    g'4
                    bf'4
                    c'4
                    a'4
                    c'4
                    d'4
                    c'4
                    ef'4
                    f'4
                }
            >>
        >>
        \new StaffGroup
        <<
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    g'4
                    b'4
                    f'4
                    c'4
                    e'4
                    cs'4
                    af'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    f'4
                    cs'4
                    g'4
                    c'4
                    af'4
                    b'4
                    e'4
                    c'4
                }
                \new Staff
                {
                    b'4
                    g'4
                    c'4
                    e'4
                    c'4
                    f'4
                    c'4
                    af'4
                    cs'4
                }
                \new Staff
                {
                    cs'4
                    f'4
                    c'4
                    af'4
                    c'4
                    g'4
                    c'4
                    e'4
                    b'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    e'4
                    f'4
                    af'4
                    c'4
                    cs'4
                    g'4
                    b'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    af'4
                    g'4
                    e'4
                    c'4
                    b'4
                    f'4
                    cs'4
                    c'4
                }
                \new Staff
                {
                    f'4
                    e'4
                    c'4
                    cs'4
                    c'4
                    af'4
                    c'4
                    b'4
                    g'4
                }
                \new Staff
                {
                    g'4
                    af'4
                    c'4
                    b'4
                    c'4
                    e'4
                    c'4
                    cs'4
                    f'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    cs'4
                    af'4
                    b'4
                    c'4
                    g'4
                    e'4
                    f'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    b'4
                    e'4
                    cs'4
                    c'4
                    f'4
                    af'4
                    g'4
                    c'4
                }
                \new Staff
                {
                    af'4
                    cs'4
                    c'4
                    g'4
                    c'4
                    b'4
                    c'4
                    f'4
                    e'4
                }
                \new Staff
                {
                    e'4
                    b'4
                    c'4
                    f'4
                    c'4
                    cs'4
                    c'4
                    g'4
                    af'4
                }
            >>
        >>
        \new StaffGroup
        <<
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    e'4
                    ef'4
                    af'4
                    c'4
                    b'4
                    a'4
                    cs'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    af'4
                    a'4
                    e'4
                    c'4
                    cs'4
                    ef'4
                    b'4
                    c'4
                }
                \new Staff
                {
                    ef'4
                    e'4
                    c'4
                    b'4
                    c'4
                    af'4
                    c'4
                    cs'4
                    a'4
                }
                \new Staff
                {
                    a'4
                    af'4
                    c'4
                    cs'4
                    c'4
                    e'4
                    c'4
                    b'4
                    ef'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    b'4
                    af'4
                    cs'4
                    c'4
                    a'4
                    e'4
                    ef'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    cs'4
                    e'4
                    b'4
                    c'4
                    ef'4
                    af'4
                    a'4
                    c'4
                }
                \new Staff
                {
                    af'4
                    b'4
                    c'4
                    a'4
                    c'4
                    cs'4
                    c'4
                    ef'4
                    e'4
                }
                \new Staff
                {
                    e'4
                    cs'4
                    c'4
                    ef'4
                    c'4
                    b'4
                    c'4
                    a'4
                    af'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    a'4
                    cs'4
                    ef'4
                    c'4
                    e'4
                    b'4
                    af'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    ef'4
                    b'4
                    a'4
                    c'4
                    af'4
                    cs'4
                    e'4
                    c'4
                }
                \new Staff
                {
                    cs'4
                    a'4
                    c'4
                    e'4
                    c'4
                    ef'4
                    c'4
                    af'4
                    b'4
                }
                \new Staff
                {
                    b'4
                    ef'4
                    c'4
                    af'4
                    c'4
                    a'4
                    c'4
                    e'4
                    cs'4
                }
            >>
        >>
        \new StaffGroup
        <<
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    b'4
                    g'4
                    cs'4
                    c'4
                    af'4
                    f'4
                    e'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    cs'4
                    f'4
                    b'4
                    c'4
                    e'4
                    g'4
                    af'4
                    c'4
                }
                \new Staff
                {
                    g'4
                    b'4
                    c'4
                    af'4
                    c'4
                    cs'4
                    c'4
                    e'4
                    f'4
                }
                \new Staff
                {
                    f'4
                    cs'4
                    c'4
                    e'4
                    c'4
                    b'4
                    c'4
                    af'4
                    g'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    af'4
                    cs'4
                    e'4
                    c'4
                    f'4
                    b'4
                    g'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    e'4
                    b'4
                    af'4
                    c'4
                    g'4
                    cs'4
                    f'4
                    c'4
                }
                \new Staff
                {
                    cs'4
                    af'4
                    c'4
                    f'4
                    c'4
                    e'4
                    c'4
                    g'4
                    b'4
                }
                \new Staff
                {
                    b'4
                    e'4
                    c'4
                    g'4
                    c'4
                    af'4
                    c'4
                    f'4
                    cs'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    f'4
                    e'4
                    g'4
                    c'4
                    b'4
                    af'4
                    cs'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    g'4
                    af'4
                    f'4
                    c'4
                    cs'4
                    e'4
                    b'4
                    c'4
                }
                \new Staff
                {
                    e'4
                    f'4
                    c'4
                    b'4
                    c'4
                    g'4
                    c'4
                    cs'4
                    af'4
                }
                \new Staff
                {
                    af'4
                    g'4
                    c'4
                    cs'4
                    c'4
                    f'4
                    c'4
                    b'4
                    e'4
                }
            >>
        >>
        \new StaffGroup
        <<
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    af'4
                    fs'4
                    e'4
                    c'4
                    bf'4
                    fs'4
                    d'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    e'4
                    fs'4
                    af'4
                    c'4
                    d'4
                    fs'4
                    bf'4
                    c'4
                }
                \new Staff
                {
                    fs'4
                    af'4
                    c'4
                    bf'4
                    c'4
                    e'4
                    c'4
                    d'4
                    fs'4
                }
                \new Staff
                {
                    fs'4
                    e'4
                    c'4
                    d'4
                    c'4
                    af'4
                    c'4
                    bf'4
                    fs'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    bf'4
                    e'4
                    d'4
                    c'4
                    fs'4
                    af'4
                    fs'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    d'4
                    af'4
                    bf'4
                    c'4
                    fs'4
                    e'4
                    fs'4
                    c'4
                }
                \new Staff
                {
                    e'4
                    bf'4
                    c'4
                    fs'4
                    c'4
                    d'4
                    c'4
                    fs'4
                    af'4
                }
                \new Staff
                {
                    af'4
                    d'4
                    c'4
                    fs'4
                    c'4
                    bf'4
                    c'4
                    fs'4
                    e'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    fs'4
                    d'4
                    fs'4
                    c'4
                    af'4
                    bf'4
                    e'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    fs'4
                    bf'4
                    fs'4
                    c'4
                    e'4
                    d'4
                    af'4
                    c'4
                }
                \new Staff
                {
                    d'4
                    fs'4
                    c'4
                    af'4
                    c'4
                    fs'4
                    c'4
                    e'4
                    bf'4
                }
                \new Staff
                {
                    bf'4
                    fs'4
                    c'4
                    e'4
                    c'4
                    fs'4
                    c'4
                    af'4
                    d'4
                }
            >>
        >>
        \new StaffGroup
        <<
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    bf'4
                    b'4
                    d'4
                    c'4
                    cs'4
                    cs'4
                    b'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    d'4
                    cs'4
                    bf'4
                    c'4
                    b'4
                    b'4
                    cs'4
                    c'4
                }
                \new Staff
                {
                    b'4
                    bf'4
                    c'4
                    cs'4
                    c'4
                    d'4
                    c'4
                    b'4
                    cs'4
                }
                \new Staff
                {
                    cs'4
                    d'4
                    c'4
                    b'4
                    c'4
                    bf'4
                    c'4
                    cs'4
                    b'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    cs'4
                    d'4
                    b'4
                    c'4
                    cs'4
                    bf'4
                    b'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    b'4
                    bf'4
                    cs'4
                    c'4
                    b'4
                    d'4
                    cs'4
                    c'4
                }
                \new Staff
                {
                    d'4
                    cs'4
                    c'4
                    cs'4
                    c'4
                    b'4
                    c'4
                    b'4
                    bf'4
                }
                \new Staff
                {
                    bf'4
                    b'4
                    c'4
                    b'4
                    c'4
                    cs'4
                    c'4
                    cs'4
                    d'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    cs'4
                    b'4
                    b'4
                    c'4
                    bf'4
                    cs'4
                    d'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    b'4
                    cs'4
                    cs'4
                    c'4
                    d'4
                    b'4
                    bf'4
                    c'4
                }
                \new Staff
                {
                    b'4
                    cs'4
                    c'4
                    bf'4
                    c'4
                    b'4
                    c'4
                    d'4
                    cs'4
                }
                \new Staff
                {
                    cs'4
                    b'4
                    c'4
                    d'4
                    c'4
                    cs'4
                    c'4
                    bf'4
                    b'4
                }
            >>
        >>
        \new StaffGroup
        <<
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    cs'4
                    bf'4
                    b'4
                    c'4
                    a'4
                    d'4
                    ef'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    b'4
                    d'4
                    cs'4
                    c'4
                    ef'4
                    bf'4
                    a'4
                    c'4
                }
                \new Staff
                {
                    bf'4
                    cs'4
                    c'4
                    a'4
                    c'4
                    b'4
                    c'4
                    ef'4
                    d'4
                }
                \new Staff
                {
                    d'4
                    b'4
                    c'4
                    ef'4
                    c'4
                    cs'4
                    c'4
                    a'4
                    bf'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    a'4
                    b'4
                    ef'4
                    c'4
                    d'4
                    cs'4
                    bf'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    ef'4
                    cs'4
                    a'4
                    c'4
                    bf'4
                    b'4
                    d'4
                    c'4
                }
                \new Staff
                {
                    b'4
                    a'4
                    c'4
                    d'4
                    c'4
                    ef'4
                    c'4
                    bf'4
                    cs'4
                }
                \new Staff
                {
                    cs'4
                    ef'4
                    c'4
                    bf'4
                    c'4
                    a'4
                    c'4
                    d'4
                    b'4
                }
            >>
            \new StaffGroup
            <<
                \new Staff
                {
                    c'4
                    d'4
                    ef'4
                    bf'4
                    c'4
                    cs'4
                    a'4
                    b'4
                    c'4
                }
                \new Staff
                {
                    c'4
                    bf'4
                    a'4
                    d'4
                    c'4
                    b'4
                    ef'4
                    cs'4
                    c'4
                }
                \new Staff
                {
                    ef'4
                    d'4
                    c'4
                    cs'4
                    c'4
                    bf'4
                    c'4
                    b'4
                    a'4
                }
                \new Staff
                {
                    a'4
                    bf'4
                    c'4
                    b'4
                    c'4
                    d'4
                    c'4
                    cs'4
                    ef'4
                }
            >>
        >>
    >>
} %! abjad.LilyPondFile._get_formatted_blocks()
