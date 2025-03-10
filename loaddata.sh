#!/bin/sh

case "1" in
  ${LOAD_INITIAL_DATA} )
  echo ${LOAD_INITIAL_DATA} &&
  yes | python manage.py makemigrations &&
  yes | python manage.py makemigrations --merge &&
  python manage.py migrate &&
  python manage.py collectstatic --no-input &&
  python manage.py loaddata CatAmbitosLaborales &&
  python manage.py loaddata CatDocumentosObtenidos &&
  python manage.py loaddata CatEntesPublicos &&
  python manage.py loaddata CatEntidadesFederativas &&
  python manage.py loaddata CatEstadosCiviles &&
  python manage.py loaddata CatEstatusDeclaracion &&
  python manage.py loaddata CatEstatusEstudios &&
  python manage.py loaddata CatFormasAdquisiciones &&
  python manage.py loaddata CatFuncionesPrincipales &&
  python manage.py loaddata CatGradosAcademicos &&
  python manage.py loaddata CatMonedas &&
  python manage.py loaddata CatNaturalezaMembresia &&
  python manage.py loaddata CatOrdenesGobierno &&
  python manage.py loaddata CatPaises &&
  python manage.py loaddata CatPoderes &&
  python manage.py loaddata CatRegimenesMatrimoniales &&
  python manage.py loaddata CatSectoresIndustria &&
  python manage.py loaddata CatTiposAcreedores &&
  python manage.py loaddata CatTiposActividad &&
  python manage.py loaddata CatTiposAdeudos &&
  python manage.py loaddata CatTiposApoyos &&
  python manage.py loaddata CatTiposBeneficios &&
  python manage.py loaddata CatTiposBienes &&
  python manage.py loaddata CatTiposDeclaracion &&
  python manage.py loaddata CatTiposInversiones &&
  python manage.py loaddata CatTiposEspecificosInversiones &&
  python manage.py loaddata CatTiposFideicomisos &&
  python manage.py loaddata CatTiposInmuebles &&
  python manage.py loaddata CatTiposInstituciones &&
  python manage.py loaddata CatTiposInstrumentos &&
  python manage.py loaddata CatTiposMetales &&
  python manage.py loaddata CatTiposMuebles &&
  python manage.py loaddata CatTiposOperaciones &&
  python manage.py loaddata CatTiposPasivos &&
  python manage.py loaddata CatTiposRelacionesPersonales &&
  python manage.py loaddata CatTiposRepresentaciones &&
  python manage.py loaddata CatTiposTitulares &&
  python manage.py loaddata CatTitularTiposRelaciones &&
  python manage.py loaddata Secciones &&
  python manage.py loaddata CatTipoPersona &&
  python manage.py loaddata CatActivoBien &&
  python manage.py loaddata CatTipoParticipacion &&
  python manage.py loaddata CatUnidadesTemporales &&
  python manage.py loaddata CatTipoVia &&
  python manage.py loaddata CatCamposObligatorios &&
  python manage.py loaddata CatMunicipios &&
  python manage.py loaddata CatMotivoBaja &&
  python manage.py loaddata faq &&
  python manage.py loaddata dumpAuthUser &&  
  python manage.py loaddata CatAreas &&
  python manage.py loaddata CatPuestos ;;
esac
echo $LOAD_INITIAL_DATA
