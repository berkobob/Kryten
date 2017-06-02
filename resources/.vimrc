"Vundle
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
" Add all your plugins here
Plugin 'tmhedberg/SimpylFold'
Plugin 'scrooloose/nerdtree'
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
Plugin 'davidhalter/jedi-vim'

" All of your Plugins must be added before the following line
call vundle#end()
filetype plugin indent on
let g:pymode_python = 'python3'

set splitbelow
set splitright
"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

"Preview a line on folds
let g:SimpylFold_docstring_preview=1

" Python spacing
au BufNewFile,BufRead *.py
    \ set tabstop=4 |
    \ set softtabstop=4 |
    \ set shiftwidth=4 |
    \ set textwidth=79 |
    \ set expandtab |
    \ set autoindent |
    \ set fileformat=unix

set encoding=utf-8
let python_highlight_all=1
syntax on
set foldlevel=99
set nu

highlight BadWhitespace ctermbg=red guibg=red
au BufRead,BufNewFile *.py,*.pyw match BadWhitespace /^\t\+/
au BufRead,BufNewFile *.py,*.pyw match BadWhitespace /\s\+$/

silent! nmap <C-o> :NERDTreeToggle<CR>

"Conque - bash in vim 
let g:ConqueTerm_PyVersion = 3
nmap <C-e> :ConqueTermVSplit bash<CR>
let g:ConqueTerm_ReadUnfocused = 1
let g:ConqueTerm_InsertOnEnter = 1
let g:ConqueTerm_CWInsert = 1
let g:ConqueTerm_ExecFileKey = '<F11>'

set backspace=indent,eol,start
