import pygame
from exceptions import exceptions_int
print("Você quer experenciar algo interessante?")
print("1-Sim \n2-Não")
escolha = exceptions_int("")
while (escolha != 1 and escolha != 2):
 print("Opção inválida, tente novamente")
 escolha = exceptions_int("Digite 1 ou 2: ")

if (escolha == 1) :
 pygame.init()
 pygame.mixer.music.load('./Musica/audio.mp3')
 pygame.mixer.music.play(0, 8, 0)
 input()
 pygame.event.wait()
else:
 pygame.init()
 pygame.mixer.music.load('./Musica/Silêncio.mp3')
 pygame.mixer.music.play(0, 10, 0)
 input()
 pygame.event.wait()


