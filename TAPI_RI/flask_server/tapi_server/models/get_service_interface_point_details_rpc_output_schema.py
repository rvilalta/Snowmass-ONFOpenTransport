# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.service_interface_point import ServiceInterfacePoint  # noqa: F401,E501
from tapi_server import util


class GetServiceInterfacePointDetailsRPCOutputSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sip: ServiceInterfacePoint=None):  # noqa: E501
        """GetServiceInterfacePointDetailsRPCOutputSchema - a model defined in Swagger

        :param sip: The sip of this GetServiceInterfacePointDetailsRPCOutputSchema.  # noqa: E501
        :type sip: ServiceInterfacePoint
        """
        self.swagger_types = {
            'sip': ServiceInterfacePoint
        }

        self.attribute_map = {
            'sip': 'sip'
        }

        self._sip = sip

    @classmethod
    def from_dict(cls, dikt) -> 'GetServiceInterfacePointDetailsRPCOutputSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get-service-interface-point-detailsRPC_output_schema of this GetServiceInterfacePointDetailsRPCOutputSchema.  # noqa: E501
        :rtype: GetServiceInterfacePointDetailsRPCOutputSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sip(self) -> ServiceInterfacePoint:
        """Gets the sip of this GetServiceInterfacePointDetailsRPCOutputSchema.


        :return: The sip of this GetServiceInterfacePointDetailsRPCOutputSchema.
        :rtype: ServiceInterfacePoint
        """
        return self._sip

    @sip.setter
    def sip(self, sip: ServiceInterfacePoint):
        """Sets the sip of this GetServiceInterfacePointDetailsRPCOutputSchema.


        :param sip: The sip of this GetServiceInterfacePointDetailsRPCOutputSchema.
        :type sip: ServiceInterfacePoint
        """

        self._sip = sip
