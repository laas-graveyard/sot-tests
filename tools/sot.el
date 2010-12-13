;;   Emacs Mode for StackOfTasks script
;;
;;   Installation:
;;
;;   Put the this file as "sot.el" somewhere on your load path, then
;;   add this to your .emacs or site-init.el file:
;;
;;   (autoload 'sot-mode "sot" "Enter Sot mode." t)
;;   (setq auto-mode-alist (cons '("\\.sot\\'" . sot-mode) auto-mode-alist))
;;   (autoload 'sot-shell "sot" "Interactive Sot mode." t)
;;
;;   sot-mode fires up automatically with all *.sot files
;;   To start up sot-mode manually do
;;       M-x sot-mode

(defvar sot-mode-hook nil)
(defvar sot-mode-map
  (let ((map (make-keymap)))
    (define-key map "\C-j" 'newline-and-indent)
    map)
  "Keymap for SOT major mode")

;; This regex is the result of
;; (regexp-opt '("plug" "new" "destrop" "run" "import"
;;     "loadPlugin" "unloadPlugin" "help"
;;     "set" "get" "compute" "try"
;;     "loadPlugin" "displayPlugins"
;;     "factory" "unplug" "dispmat"
;;     "clearPlugin" "signalTime" "synchro"
;;     "echo" "copy" "freeze" "squeeze"
;;     "debugtrace" "prompt" "sleep"
;;     "setflag" "completion" ) t)
(defconst sot-font-lock-keywords-1
  (list '("\\<\\(c\\(?:learPlugin\\|o\\(?:mp\\(?:letion\\|ute\\)\\|py\\)\\)\\|d\\(?:e\\(?:bugtrace\\|strop\\)\\|isp\\(?:layPlugins\\|mat\\)\\)\\|echo\\|f\\(?:actory\\|reeze\\)\\|get\\|help\\|import\\|loadPlugin\\|new\\|p\\(?:lug\\|rompt\\)\\|run\\|s\\(?:et\\(?:flag\\)?\\|ignalTime\\|leep\\|queeze\\|ynchro\\)\\|try\\|un\\(?:loadPlugin\\|plug\\)\\)\\>" . font-lock-keyword-face))
  "Minimal highlighting expressions for SOT mode")

(defvar sot-font-lock-keywords sot-font-lock-keywords-1
  "Default highlighting expressions for SOT mode")

(defvar sot-mode-syntax-table
  (let ((st (make-syntax-table)))
    ;; make to the syntax table is to declare the underscore character ‘_’
    ;; as being a valid part of a word
    (modify-syntax-entry ?_ "w" st)
    (modify-syntax-entry ?# ". 1b" st)
    (modify-syntax-entry ?\s ". 2" st)
    (modify-syntax-entry ?\n ">" st)
    st)
  "Syntax table for sot-mode")

(defun sot-mode ()
  "Major mode for editing sot script files"
  (interactive)
  (kill-all-local-variables)
  (set-syntax-table sot-mode-syntax-table)
  (set (make-local-variable 'font-lock-defaults) '(sot-font-lock-keywords))
  (setq major-mode 'sot-mode)
  (setq mode-name "SOT")
  (run-hooks 'sot-mode-hook))

(provide 'sot-mode)

