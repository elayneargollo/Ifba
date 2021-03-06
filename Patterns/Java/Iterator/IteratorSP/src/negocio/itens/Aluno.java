package negocio.itens;

import interfaces.IAgregavel;

public class Aluno implements IAgregavel {
	
	private String nome;
	private String sexo;
	private String turma;
	private double media;
	
	public Aluno(String nome, String sexo, String turma, double media) {
		this.nome = nome;
		this.sexo = sexo;
		this.turma = turma;
		this.media = media;
	}
	
	@Override
	public String nome() {
		return nome;
	}
	
	public String sexo() {
		return sexo;
	}
	
	public String turma() {
		return turma;
	}
	
	public double media() {
		return media;
	}

}
