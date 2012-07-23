"" general
filetype off                   " required!
call pathogen#runtime_append_all_bundles()
filetype plugin indent on
set nocompatible               " be iMproved
set modelines=0

"" good stuff
syntax on
set number
set laststatus=2                " Always show the statusline
set encoding=utf-8
set scrolloff=3
set autoindent
set showmode
set showcmd
set hidden
set wildmenu
set wildmode=list:longest
set visualbell
set cursorline
set ttyfast
set ruler
set backspace=indent,eol,start
set laststatus=2
set relativenumber      "" changes Vim’s line number column to display how far away each line is from the current one
set undofile
set directory=~/.vim/tmp
set noerrorbells
set ruler

"" tabs
set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab
set nofsync
set swapsync=

"" change the leader key
let mapleader = ","

""" searching/moving
nnoremap / /\v
vnoremap / /\v
set ignorecase
set smartcase
set gdefault
set incsearch
set showmatch
set hlsearch
nnoremap <leader><space> :noh<cr> "" clear a search result
nnoremap <tab> %
vnoremap <tab> %

"" handling long lines
set wrap
set textwidth=79
set formatoptions=qrn1
set colorcolumn=85

"" hardcore Vim, disable arrows to force you to use hjkl :-)
nnoremap <up> <nop>
nnoremap <down> <nop>
nnoremap <left> <nop>
nnoremap <right> <nop>
inoremap <up> <nop>
inoremap <down> <nop>
inoremap <left> <nop>
inoremap <right> <nop>
nnoremap j gj
nnoremap k gk

"" save on losing focus
au FocusLost * :wa


"" Fun with the Leader
"" strip all trailing whitespace in the current file
nnoremap <leader>W :%s/\s\+$//<cr>:let @/=''<CR>

"" split windows fun
nnoremap <leader>w <C-w>v<C-w>l  "" open a new vertical window and go for it


"""""""""""""""""""" PLUGINS

set guifont=DejaVu\ Sans\ Mono\ for\ Powerline\ 10
let g:Powerline_symbols = 'fancy'
let g:CommandTMaxFiles=5000
let g:CommandTMaxHeight=12
map <C-o> :CommandT<CR>
let g:CommandTAcceptSelectionMap = '<CR>'
let g:CommandTCancelMap = '<C-g>'

let NERDChristmasTree = 1
let NERDTreeSortOrder = ['\/$', '\.js*', '\.cpp$', '\.h$', '*']
nmap <c-b> :NERDTreeToggle<cr>
nmap <C-n> <c-w><left><down><c-w><c-w>
nmap <C-p> <c-w><left><up><c-w><c-w>
nmap <C-o> <c-w><left><CR>

set fillchars+=stl:\ ,stlnc:\
